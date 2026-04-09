# ⚠️ Generador FMEA con IA

[![CC BY 4.0][cc-by-shield]][cc-by]
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.55+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5.4-412991?style=flat&logo=openai&logoColor=white)](https://openai.com/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Conda](https://img.shields.io/badge/Conda-Environment-44A833?style=flat&logo=anaconda&logoColor=white)](https://docs.conda.io/)

Aplicación web para generar análisis FMEA (Failure Mode and Effects Analysis) automáticamente a partir de los pasos de un proceso, utilizando la API de OpenAI.

> **⚠️ IMPORTANTE - Consideraciones de Uso**
> 
> Esta herramienta genera análisis FMEA automatizados que deben considerarse como **insumo inicial** para el análisis formal. El análisis FMEA definitivo y las decisiones relacionadas con la gestión de riesgos son responsabilidad del **responsable del proceso y su equipo de trabajo**. 
> 
> Se recomienda:
> - Revisar y validar todos los modos de fallo generados
> - Ajustar las calificaciones de Severidad, Ocurrencia y Detección según el conocimiento experto del proceso
> - Complementar con la experiencia del equipo y datos históricos
> - Utilizar como punto de partida para discusiones de mejora continua

---

## 📑 Tabla de Contenido

- [🌟 Características Principales](#-características-principales)
- [📋 Requisitos Previos](#-requisitos-previos)
- [🚀 Instalación](#-instalación)
- [▶️ Uso](#️-uso)
- [📊 Formato de Excel de Entrada](#-formato-de-excel-de-entrada)
- [📈 Interpretación de Resultados](#-interpretación-de-resultados)
- [🎯 Características Avanzadas](#-características-avanzadas)
- [💡 Consejos de Uso](#-consejos-de-uso)
- [🛠️ Estructura del Proyecto](#️-estructura-del-proyecto)
- [🐛 Solución de Problemas](#-solución-de-problemas)
- [📚 Referencias](#-referencias)
- [📄 Licencia](#-licencia)

---

[cc-by]: https://creativecommons.org/licenses/by/4.0/deed.es
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## 🌟 Características Principales

### 🚀 Generación Inteligente de FMEA
- **IA de última generación**: Utiliza GPT-5.4 de OpenAI para análisis profundos y precisos
- **Generación automática completa**: Crea modos de fallo, efectos, causas, controles y acciones recomendadas
- **Múltiples escenarios por paso**: Configurable de 1 a 5 modos de fallo por cada paso del proceso
- **Evaluación experta**: Asigna valores realistas de Severidad (S), Ocurrencia (O) y Detección (D) en escala 1-10
- **Cálculo automático de RPN**: Risk Priority Number = S × O × D calculado automáticamente

### 📊 Análisis y Visualización
- **Dashboard de métricas**: Vista instantánea con total de items, RPN promedio, riesgos altos y RPN máximo
- **Distribución de riesgos**: Categorización automática en riesgo bajo (<50), medio (50-100) y alto (>100)
- **Top 5 riesgos**: Identificación inmediata de los mayores riesgos del proceso
- **Vista tabular completa**: Visualización organizada de todos los campos del FMEA

### ✏️ Edición Interactiva
- **Editor en tiempo real**: Modifica cualquier valor directamente en la tabla
- **Validación automática**: Asegura que S, O, D estén en rango 1-10
- **Recálculo dinámico**: El RPN se actualiza automáticamente al cambiar S, O o D
- **Agregar/eliminar filas**: Gestión flexible de items del FMEA
- **Columnas editables y protegidas**: Algunas columnas bloqueadas para mantener integridad de datos

### 📥 Importación y Validación
- **Carga de Excel flexible**: Acepta diferentes formatos y nomenclaturas de columnas
- **Validación inteligente**: Detecta automáticamente la columna de descripción del proceso
- **Preview de datos**: Vista previa del archivo cargado antes de generar el análisis
- **Detección de errores**: Mensajes claros sobre problemas en el formato del archivo
- **Template incluido**: Archivo de ejemplo (`template_proceso.xlsx`) con estructura recomendada

### 💾 Exportación Profesional
- **Formato Excel completo**: Exporta con estilos profesionales y colores corporativos
- **Formato condicional inteligente**: 
  - 🟢 Verde para RPN < 50 (riesgo bajo)
  - 🟡 Amarillo para RPN 50-100 (riesgo medio)
  - 🔴 Rojo para RPN > 100 (riesgo alto)
- **Filtros automáticos**: Todas las columnas con capacidad de filtrado
- **Ajuste de columnas**: Ancho optimizado según contenido
- **Encabezados formateados**: Títulos destacados y profesionales

### 🌐 Configuración y Personalización
- **Soporte multiidioma**: Interfaz y análisis en Español o Inglés
- **Prompts externalizados y editables**: 
  - Plantillas de prompts en archivos markdown separados
  - Fácil personalización sin tocar código Python
  - Agrega nuevos idiomas simplemente creando archivos
  - Ajusta escalas y formato según necesidades corporativas
- **Gestión segura de API Key**: 
  - Carga exclusivamente desde archivo `.env`
  - No permite ingreso manual (mayor seguridad)
  - Nunca muestra la key en pantalla
  - Archivo `.env` protegido en `.gitignore`
- **Modos de fallo configurables**: Ajusta la cantidad según complejidad del proceso
- **Barra de progreso**: Feedback visual durante la generación del análisis
- **Sesión persistente**: Los datos generados se mantienen durante la sesión

### 📚 Ayuda Integrada
- **Documentación en la app**: Tab completo de ayuda con explicación de FMEA
- **Escalas detalladas**: Guía completa de interpretación de S, O, D y RPN
- **Ejemplo de Excel**: Formato recomendado con explicación de columnas
- **Consejos de uso**: Mejores prácticas para obtener resultados óptimos
- **Enlaces a recursos**: Referencias a estándares AIAG, ISO y documentación de OpenAI

## 📋 Requisitos Previos

- Python 3.8 o superior
- Cuenta de OpenAI con API Key ([Obtener aquí](https://platform.openai.com/api-keys))

## 🚀 Instalación

1. **Clonar o descargar este repositorio**

2. **Crear un ambiente conda** (recomendado)
   ```bash
   conda create -n fmea python=3.11 -y
   ```

3. **Instalar dependencias**
   ```bash
   # Instalar paquetes desde conda
   conda install -n fmea pandas openpyxl python-dotenv streamlit -y
   
   # Instalar OpenAI con pip (no disponible en conda)
   conda run -n fmea pip install openai
   ```
   
   **Alternativa**: Si prefieres usar pip para todo:
   ```bash
   conda activate fmea
   pip install -r requirements.txt
   ```

4. **Configurar la API Key de OpenAI** (Obligatorio)
   
   Crea un archivo `.env` en el directorio del proyecto:
   ```bash
   copy .env.example .env
   ```
   
   Edita el archivo `.env` y agrega tu API key de OpenAI:
   ```
   OPENAI_API_KEY=sk-tu-api-key-aqui
   ```
   
   > **Importante**: La aplicación solo funcionará si la API key está configurada en el archivo `.env`

## ▶️ Uso

### 🎬 Inicio Rápido

1. **Iniciar la aplicación**
   ```bash
   conda run -n fmea streamlit run app.py
   ```
   
   O si prefieres activar el ambiente primero:
   ```bash
   conda activate fmea
   streamlit run app.py
   ```

2. **Acceder a la interfaz web**
   - La aplicación se abrirá automáticamente en `http://localhost:8501`
   - Si no se abre, accede manualmente a esa URL

### 📝 Flujo de Trabajo Completo

#### 1️⃣ **Configuración** (Barra Lateral)
- ✅ **API Key**: Verifica que esté configurada correctamente (se carga desde `.env`)
- 🌐 **Idioma**: Selecciona Español o English para el análisis
- 📊 **Modos de fallo**: Ajusta cuántos escenarios generar por paso (1-5, recomendado: 2-3)

#### 2️⃣ **Carga de Proceso** (Tab: 📤 Cargar Proceso)
- Haz clic en "Browse files" o arrastra tu archivo Excel
- Visualiza el preview de tus datos cargados
- La app valida automáticamente el formato
- Si todo está correcto, aparece el botón "🚀 Generar Análisis FMEA"

#### 3️⃣ **Generación de FMEA**
- Haz clic en "🚀 Generar Análisis FMEA"
- Observa la barra de progreso mientras la IA trabaja:
  - ⏳ Enviando solicitud a OpenAI...
  - 🔄 Procesando respuesta...
  - ✅ ¡FMEA generado exitosamente!
- ¡Celebración con confetti! 🎉

#### 4️⃣ **Análisis y Edición** (Tab: 🔍 Análisis FMEA)
- **Revisa las métricas principales**:
  - Total de items generados
  - RPN promedio del proceso
  - Cantidad de riesgos altos
  - RPN máximo encontrado

- **Explora los datos**:
  - Tabla interactiva con todos los campos del FMEA
  - Edita valores directamente en las celdas
  - Agrega o elimina filas según necesites
  - Observa el recálculo automático del RPN

- **Analiza la distribución de riesgos**:
  - Gráfica de cantidad por categoría (Bajo/Medio/Alto)
  - Top 5 riesgos más críticos

#### 5️⃣ **Exportación** (Tab: 🔍 Análisis FMEA)
- Define el nombre de tu archivo de salida
- Haz clic en "📥 Descargar Excel"
- Obtén un archivo Excel profesional con:
  - ✅ Formato condicional por colores según RPN
  - ✅ Filtros automáticos en todas las columnas
  - ✅ Encabezados formateados
  - ✅ Columnas ajustadas al contenido

#### 6️⃣ **Consulta la Ayuda** (Tab: 📊 Ayuda)
- Definiciones completas de FMEA
- Escalas de Severidad, Ocurrencia y Detección
- Interpretación del RPN
- Formato recomendado de Excel
- Mejores prácticas y consejos

### ⚡ Inicio Rápido con Script

Para Windows, simplemente ejecuta:
```bash
run_app.bat
```

Este script automáticamente activa el ambiente conda y lanza la aplicación.

## 📊 Formato de Excel de Entrada

Tu archivo Excel debe contener los pasos de tu proceso. Se recomienda la siguiente estructura:

| Número | Descripción | Responsable | Entradas | Salidas |
|--------|-------------|-------------|----------|---------|
| 1 | Recepción de materia prima | Almacén | Orden de compra, Material | Material verificado |
| 2 | Inspección de calidad | Control de Calidad | Material | Reporte de inspección |
| 3 | Almacenamiento temporal | Almacén | Material aprobado | Material almacenado |

**Columnas requeridas**:
- Al menos una columna con la descripción del paso (puede llamarse: Descripción, Description, Paso, Actividad, etc.)

**Columnas opcionales** (mejoran el análisis):
- Número de paso
- Responsable
- Entradas
- Salidas
- Recursos
- Procedimiento

> **Nota**: Puedes usar el archivo `template_proceso.xlsx` como referencia.

## 📈 Interpretación de Resultados

### Escalas de Evaluación

#### Severidad (S): 1-10
Gravedad del efecto del fallo:
- **10**: Peligroso sin advertencia
- **7-9**: Muy alta a peligrosa con advertencia
- **4-6**: Moderada a baja
- **1-3**: Mínima o sin efecto

#### Ocurrencia (O): 1-10
Probabilidad de que ocurra la causa:
- **10**: Casi inevitable (≥1 en 2)
- **7-9**: Alta frecuencia
- **4-6**: Moderada
- **1-3**: Remota a casi imposible

#### Detección (D): 1-10
Capacidad de detectar el fallo:
- **10**: Imposible de detectar
- **7-9**: Muy difícil de detectar
- **4-6**: Moderadamente detectable
- **1-3**: Muy fácil de detectar

### RPN (Risk Priority Number)

**RPN = Severidad × Ocurrencia × Detección**

- **RPN > 100**: ⚠️ **Riesgo Alto** - Requiere acción inmediata
- **50 ≤ RPN ≤ 100**: ⚡ **Riesgo Medio** - Requiere atención
- **RPN < 50**: ✅ **Riesgo Bajo** - Monitorear

## 🎯 Características Avanzadas

### Modelo de IA

La aplicación utiliza **GPT-5.4**, el modelo frontera de OpenAI, que proporciona:
- Análisis de alta calidad y precisión
- Comprensión contextual profunda de procesos
- Evaluaciones realistas de Severidad, Ocurrencia y Detección
- Sugerencias de acciones correctivas específicas y útiles

### Configuraciones Personalizables

- **API Key**: Se configura únicamente desde archivo `.env` (mayor seguridad)
- **Modos de fallo por paso**: Controla cuántos escenarios de fallo generar (1-5)
- **Idioma**: Genera el análisis en Español o Inglés
- **Edición en vivo**: Modifica cualquier valor y el RPN se recalcula automáticamente

### Formato de Exportación

El Excel exportado incluye:
- ✅ Encabezados formateados con color
- ✅ Formato condicional por RPN:
  - 🟢 Verde: RPN < 50
  - 🟡 Amarillo: 50 ≤ RPN ≤ 100
  - 🔴 Rojo: RPN > 100
- ✅ Filtros automáticos en todas las columnas
- ✅ Ancho de columnas ajustado automáticamente

## 🔒 Seguridad y Privacidad

- ⚠️ **Protección de API Keys**: 
  - Nunca subas archivos `.env` a repositorios públicos
  - El archivo `.env` está incluido en `.gitignore` por seguridad
  - La API key solo se carga desde el archivo `.env` (no se permite ingreso manual)
- 🔐 **Datos del proceso**: Los datos se envían a OpenAI para el análisis. Revisa los términos de servicio de OpenAI
- 💾 **Datos locales**: La aplicación no almacena tus datos. Todo se procesa en memoria

## 💡 Consejos de Uso

1. **⚠️ Herramienta de apoyo**: Esta aplicación genera un **borrador inicial** de FMEA. El análisis final debe ser validado y completado por el responsable del proceso y su equipo de trabajo, quienes conocen mejor los detalles operativos
2. **API Key**: Asegúrate de configurar el archivo `.env` con tu `OPENAI_API_KEY` antes de iniciar
3. **Procesos simples**: Usa 2 modos de fallo por paso para análisis rápidos y enfocados
4. **Procesos complejos**: Aumenta a 3-4 modos de fallo para análisis exhaustivos
5. **Edición**: Siempre revisa y ajusta los valores según tu experiencia del proceso
6. **Priorización**: Enfócate primero en items con RPN > 100
7. **Reinicio**: Si cambias la API key en `.env`, reinicia la aplicación para que tome efecto

## 🛠️ Estructura del Proyecto

```
fmea/
├── app.py                  # Aplicación Streamlit principal
├── fmea_generator.py       # Lógica de generación FMEA con OpenAI
├── requirements.txt        # Dependencias del proyecto
├── .env.example           # Plantilla de configuración
├── .gitignore             # Archivos a ignorar en Git
├── LICENSE                # Licencia Creative Commons BY 4.0
├── README.md              # Este archivo
├── template_proceso.xlsx  # Ejemplo de archivo de entrada
├── run_app.bat            # Script de inicio para Windows
└── prompts/               # Plantillas de prompts para la IA
    ├── fmea_prompt_es.md  # Prompt en español (personalizable)
    └── fmea_prompt_en.md  # Prompt en inglés (personalizable)
```

### 📝 Personalización de Prompts

Los prompts utilizados para generar el análisis FMEA están almacenados en archivos markdown en la carpeta `prompts/`. Esto te permite:

- ✏️ **Personalizar las instrucciones** para la IA según tus necesidades específicas
- 🌐 **Agregar nuevos idiomas** creando archivos `fmea_prompt_XX.md` (donde XX es el código del idioma)
- 🎯 **Ajustar las escalas** de Severidad, Ocurrencia y Detección según estándares corporativos
- 📋 **Modificar el formato de salida** para incluir campos adicionales
- 🔄 **Versionar los prompts** independientemente del código Python

Los prompts utilizan placeholders que se reemplazan automáticamente:
- `{num_failures}`: Número de modos de fallo por paso
- `{process_steps}`: Lista enumerada de los pasos del proceso

> **Nota**: Después de modificar los prompts, simplemente recarga la página en Streamlit para que los cambios tomen efecto.

## 🐛 Solución de Problemas

### Error: "Invalid API Key" o "API Key no configurada"
- Verifica que el archivo `.env` exista en el directorio del proyecto
- Abre el archivo `.env` y confirma que la API key esté correctamente escrita (empieza con `sk-`)
- Asegúrate de tener créditos disponibles en tu cuenta de OpenAI
- Reinicia la aplicación después de modificar el archivo `.env`
- No incluyas espacios ni comillas extras: `OPENAI_API_KEY=sk-tu-key-aqui`

### Error: "No se encontró columna de descripción"
- Verifica que tu Excel tenga una columna con la descripción de los pasos
- Los nombres válidos incluyen: Descripción, Description, Paso, Actividad, etc.

### La aplicación no inicia
- Verifica que todas las dependencias estén instaladas
- Verifica que el ambiente conda esté activo o uses `conda run -n fmea`
- Lista los paquetes instalados: `conda list -n fmea`

### El análisis tarda mucho
- Es normal para procesos grandes (el modelo GPT-5.4 analiza en profundidad)
- Para procesos muy grandes (>20 pasos), considera dividirlos en secciones
- El tiempo depende de la carga de OpenAI y tu conexión a internet

## 📚 Referencias

- [AIAG FMEA Handbook](https://www.aiag.org/)
- [ISO 31010:2019 - Risk Assessment Techniques](https://www.iso.org/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 📄 Licencia

Este proyecto está licenciado bajo la [Licencia Creative Commons Attribution 4.0 Internacional (CC BY 4.0)](LICENSE).

Eres libre de:
- ✅ **Compartir** — copiar y redistribuir el material en cualquier medio o formato
- ✅ **Adaptar** — remezclar, transformar y construir a partir del material para cualquier propósito, incluso comercialmente

Bajo el siguiente término:
- 📝 **Atribución** — Debes dar crédito adecuado a Quality Analytics, proporcionar un enlace a la licencia e indicar si se realizaron cambios.

Para más detalles, consulta el archivo [LICENSE](LICENSE) o visita [creativecommons.org/licenses/by/4.0/deed.es](https://creativecommons.org/licenses/by/4.0/deed.es)

## 🤝 Contribuciones

Sugerencias y mejoras son bienvenidas. Por favor, reporta cualquier problema o sugerencia.

## 📧 Soporte

Para preguntas o soporte, contacta al equipo de Quality Analytics.

---

**Desarrollado usando Streamlit y OpenAI | © 2026 Quality Analytics**
