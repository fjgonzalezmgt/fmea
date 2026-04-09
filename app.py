"""
Aplicación Streamlit para Generación Automática de FMEA con OpenAI
"""
import streamlit as st
import pandas as pd
from io import BytesIO
import os
from dotenv import load_dotenv
from fmea_generator import FMEAGenerator

# Cargar variables de entorno
load_dotenv()

# Configuración de la página
st.set_page_config(
    page_title="Generador FMEA con IA",
    page_icon="⚠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<p class="main-header">⚠️ Generador FMEA con IA</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Análisis de Modos de Fallo y Efectos potenciado por OpenAI</p>', unsafe_allow_html=True)

# Sidebar - Configuración
st.sidebar.header("⚙️ Configuración")

# API Key
api_key_env = os.getenv("OPENAI_API_KEY", "")
if api_key_env:
    api_key = api_key_env
    st.sidebar.success("✅ API Key configurada desde archivo .env")
else:
    api_key = st.sidebar.text_input(
        "🔑 OpenAI API Key",
        type="password",
        help="Ingresa tu API key de OpenAI. Puedes obtenerla en https://platform.openai.com/api-keys"
    )
    if not api_key:
        st.sidebar.error("⚠️ API Key requerida para usar la aplicación")

# Modelo fijo
model = "gpt-5.4"

# Idioma
language = st.sidebar.selectbox(
    "🌐 Idioma",
    options=[("Español", "es"), ("English", "en")],
    format_func=lambda x: x[0],
    index=0
)

# Número de modos de fallo
num_failures = st.sidebar.slider(
    "📊 Modos de fallo por paso",
    min_value=1,
    max_value=5,
    value=2,
    help="Número de modos de fallo a generar para cada paso del proceso"
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📋 Instrucciones
1. Sube un archivo Excel con los pasos de tu proceso
2. El archivo debe tener al menos una columna con la descripción de cada paso
3. Haz clic en 'Generar FMEA'
4. Revisa y edita los resultados
5. Descarga el análisis en Excel
""")

# Inicializar session state
if 'fmea_df' not in st.session_state:
    st.session_state.fmea_df = None
if 'process_df' not in st.session_state:
    st.session_state.process_df = None

# Tabs principales
tab1, tab2, tab3 = st.tabs(["📤 Cargar Proceso", "🔍 Análisis FMEA", "📊 Ayuda"])

with tab1:
    st.header("📤 Carga tu archivo de proceso")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Selecciona un archivo Excel (.xlsx)",
            type=['xlsx'],
            help="El archivo debe contener los pasos de tu proceso. Se recomienda incluir columnas como: Número, Descripción, Responsable, Entradas, Salidas"
        )
    
    with col2:
        st.info("""
        **Formato sugerido:**
        - Número de Paso
        - Descripción
        - Responsable (opcional)
        - Entradas (opcional)
        - Salidas (opcional)
        """)
    
    if uploaded_file is not None:
        try:
            # Leer archivo
            process_df = pd.read_excel(uploaded_file)
            st.session_state.process_df = process_df
            
            st.success(f"✅ Archivo cargado exitosamente: {len(process_df)} pasos encontrados")
            
            # Mostrar preview
            st.subheader("Vista previa del proceso")
            st.dataframe(process_df, use_container_width=True, height=300)
            
            # Validar con el generador
            if api_key:
                try:
                    generator = FMEAGenerator(api_key, language=language[1])
                    is_valid, error_msg = generator.validate_process_data(process_df)
                    
                    if not is_valid:
                        st.error(f"❌ {error_msg}")
                    else:
                        st.success("✅ El archivo tiene el formato correcto")
                        
                        # Botón para generar FMEA
                        st.markdown("---")
                        if st.button("🚀 Generar Análisis FMEA", type="primary", use_container_width=True):
                            with st.spinner("Generando análisis FMEA... Esto puede tomar unos momentos."):
                                progress_bar = st.progress(0)
                                status_text = st.empty()
                                
                                def update_progress(value, message):
                                    progress_bar.progress(value)
                                    status_text.text(message)
                                
                                try:
                                    fmea_df = generator.generate_fmea(
                                        process_df,
                                        num_failures=num_failures,
                                        progress_callback=update_progress
                                    )
                                    st.session_state.fmea_df = fmea_df
                                    progress_bar.progress(1.0)
                                    status_text.empty()
                                    st.success("✅ ¡FMEA generado exitosamente! Ve a la pestaña 'Análisis FMEA' para ver los resultados.")
                                    st.balloons()
                                    
                                except Exception as e:
                                    st.error(f"❌ Error al generar FMEA: {str(e)}")
                                    progress_bar.empty()
                                    status_text.empty()
                
                except Exception as e:
                    st.warning(f"⚠️ No se pudo validar el archivo: {str(e)}")
            else:
                st.warning("⚠️ Ingresa tu API Key de OpenAI en la barra lateral para continuar")
                
        except Exception as e:
            st.error(f"❌ Error al leer el archivo: {str(e)}")
    else:
        st.info(" Sube un archivo Excel para comenzar")

with tab2:
    st.header("🔍 Análisis FMEA Generado")
    
    if st.session_state.fmea_df is not None:
        fmea_df = st.session_state.fmea_df
        
        # Estadísticas
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Items FMEA", len(fmea_df))
        
        with col2:
            avg_rpn = fmea_df['RPN'].mean()
            st.metric("RPN Promedio", f"{avg_rpn:.1f}")
        
        with col3:
            high_risk = len(fmea_df[fmea_df['RPN'] > 100])
            st.metric("Riesgos Altos (RPN>100)", high_risk)
        
        with col4:
            max_rpn = fmea_df['RPN'].max()
            st.metric("RPN Máximo", int(max_rpn))
        
        st.markdown("---")
        
        # Definir configuración de columnas para el editor
        column_config = {
            "numero_paso": st.column_config.NumberColumn("N° Paso", width="small", disabled=True),
            "paso_proceso": st.column_config.TextColumn("Paso del Proceso", width="medium"),
            "modo_fallo": st.column_config.TextColumn("Modo de Fallo", width="medium"),
            "efecto_fallo": st.column_config.TextColumn("Efecto del Fallo", width="medium"),
            "severidad": st.column_config.NumberColumn("S", min_value=1, max_value=10, width="small"),
            "causa_potencial": st.column_config.TextColumn("Causa Potencial", width="medium"),
            "ocurrencia": st.column_config.NumberColumn("O", min_value=1, max_value=10, width="small"),
            "controles_actuales": st.column_config.TextColumn("Controles Actuales", width="medium"),
            "deteccion": st.column_config.NumberColumn("D", min_value=1, max_value=10, width="small"),
            "RPN": st.column_config.NumberColumn("RPN", width="small", disabled=True),
            "acciones_recomendadas": st.column_config.TextColumn("Acciones Recomendadas", width="medium")
        }
        
        # Editor de datos
        st.subheader("📝 Editor Interactivo")
        st.info("💡 Puedes editar los valores directamente en la tabla. Los valores de S, O, D deben estar entre 1 y 10. El RPN se recalcula automáticamente.")
        
        edited_df = st.data_editor(
            fmea_df,
            column_config=column_config,
            use_container_width=True,
            num_rows="dynamic",
            height=400,
            hide_index=True
        )
        
        # Recalcular RPN si se editaron S, O, D
        if 'severidad' in edited_df.columns and 'ocurrencia' in edited_df.columns and 'deteccion' in edited_df.columns:
            edited_df['RPN'] = edited_df['severidad'] * edited_df['ocurrencia'] * edited_df['deteccion']
            st.session_state.fmea_df = edited_df
        
        # Mostrar tabla de resumen por riesgo
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Distribución de Riesgos")
            risk_distribution = pd.DataFrame({
                'Categoría': ['Bajo (RPN<50)', 'Medio (50≤RPN≤100)', 'Alto (RPN>100)'],
                'Cantidad': [
                    len(edited_df[edited_df['RPN'] < 50]),
                    len(edited_df[(edited_df['RPN'] >= 50) & (edited_df['RPN'] <= 100)]),
                    len(edited_df[edited_df['RPN'] > 100])
                ]
            })
            st.dataframe(risk_distribution, hide_index=True, use_container_width=True)
        
        with col2:
            st.subheader("⚠️ Top 5 Riesgos por RPN")
            top_risks = edited_df.nlargest(5, 'RPN')[['paso_proceso', 'modo_fallo', 'RPN']]
            st.dataframe(top_risks, hide_index=True, use_container_width=True)
        
        # Botón de descarga
        st.markdown("---")
        st.subheader("💾 Exportar Análisis")
        
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            download_filename = st.text_input("Nombre del archivo", value="analisis_fmea.xlsx")
        
        with col2:
            st.write("")  # Espaciador
            st.write("")  # Espaciador
            
            # Crear archivo Excel en memoria
            output = BytesIO()
            
            # Usar el generador para exportar con formato
            temp_file = "temp_fmea.xlsx"
            try:
                if api_key:
                    generator = FMEAGenerator(api_key, language=language[1])
                    generator.export_to_excel(edited_df, temp_file)
                    
                    # Leer el archivo formateado
                    with open(temp_file, 'rb') as f:
                        excel_data = f.read()
                    
                    # Limpiar archivo temporal
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                    
                    st.download_button(
                        label="📥 Descargar Excel",
                        data=excel_data,
                        file_name=download_filename if download_filename.endswith('.xlsx') else f"{download_filename}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        type="primary",
                        use_container_width=True
                    )
                else:
                    # Descarga simple sin formato
                    edited_df.to_excel(output, index=False)
                    st.download_button(
                        label="📥 Descargar Excel",
                        data=output.getvalue(),
                        file_name=download_filename if download_filename.endswith('.xlsx') else f"{download_filename}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        type="primary",
                        use_container_width=True
                    )
            except Exception as e:
                st.error(f"Error al generar archivo: {str(e)}")
                # Fallback a descarga simple
                edited_df.to_excel(output, index=False)
                st.download_button(
                    label="📥 Descargar Excel (sin formato)",
                    data=output.getvalue(),
                    file_name=download_filename if download_filename.endswith('.xlsx') else f"{download_filename}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
        
    else:
        st.info("ℹ️ No hay análisis FMEA generado aún. Ve a la pestaña 'Cargar Proceso' y genera un análisis primero.")

with tab3:
    st.header("📊 Ayuda y Guía de Uso")
    
    st.markdown("""
    ### ¿Qué es FMEA?
    
    **FMEA (Failure Mode and Effects Analysis)** es una metodología sistemática para identificar y prevenir problemas 
    potenciales en productos y procesos. Se utiliza ampliamente en manufactura, ingeniería de calidad, y sistemas de gestión.
    
    ### Escalas de Evaluación
    
    #### Severidad (S): 1-10
    - **10**: Peligro sin advertencia
    - **7-9**: Muy alta a peligrosa
    - **4-6**: Baja a moderada
    - **1-3**: Mínima o sin efecto
    
    #### Ocurrencia (O): 1-10
    - **10**: Casi inevitable (≥1 en 2)
    - **7-9**: Alta frecuencia
    - **4-6**: Moderada
    - **1-3**: Remota o casi imposible
    
    #### Detección (D): 1-10
    - **10**: Imposible de detectar
    - **7-9**: Muy difícil de detectar
    - **4-6**: Moderadamente detectable
    - **1-3**: Muy fácil de detectar
    
    ### RPN (Risk Priority Number)
    
    **RPN = Severidad × Ocurrencia × Detección**
    
    - **RPN > 100**: Riesgo alto - requiere acción inmediata
    - **50 ≤ RPN ≤ 100**: Riesgo medio - requiere atención
    - **RPN < 50**: Riesgo bajo - monitorear
    
    ### Formato de Excel Recomendado
    
    Tu archivo Excel debe incluir al menos:
    - **Columna obligatoria**: Descripción del paso/actividad
    - **Columnas opcionales**: Número, Responsable, Entradas, Salidas, Procedimiento
    
    Ejemplo:
    
    | Número | Descripción | Responsable | Entradas | Salidas |
    |--------|-------------|-------------|----------|---------|
    | 1 | Recepción de materia prima | Almacén | Orden de compra | Material verificado |
    | 2 | Inspección de calidad | Control de calidad | Material | Reporte de inspección |
    
    ### Consejos de Uso
    
    1. **API Key**: Obtén tu clave en [OpenAI Platform](https://platform.openai.com/api-keys)
    2. **Modelo**: La aplicación usa GPT-5.4, el modelo frontera de OpenAI
    3. **Modos de fallo**: Empieza con 2-3 por paso para obtener resultados enfocados
    4. **Edición**: Revisa y ajusta los valores generados según tu conocimiento del proceso
    5. **Acciones**: Prioriza acciones para items con RPN > 100
    
    ### Soporte
    
    Para más información sobre FMEA, consulta:
    - [AIAG FMEA Handbook](https://www.aiag.org/)
    - [ISO 31010:2019 - Risk Assessment Techniques](https://www.iso.org/)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>Desarrollado usando Streamlit y OpenAI | © 2026 Quality Analytics</p>
    <p style='font-size: 0.9em; margin-top: 0.5rem;'>
        Licenciado bajo <a href='https://creativecommons.org/licenses/by/4.0/deed.es' target='_blank' style='color: #1f77b4;'>Creative Commons BY 4.0</a>
    </p>
</div>
""", unsafe_allow_html=True)
