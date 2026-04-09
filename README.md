# ⚠️ Generador FMEA con IA

[![CC BY 4.0][cc-by-shield]][cc-by]
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.55+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5.4-412991?style=flat&logo=openai&logoColor=white)](https://openai.com/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Conda](https://img.shields.io/badge/Conda-Environment-44A833?style=flat&logo=anaconda&logoColor=white)](https://docs.conda.io/)

Aplicación web para generar análisis FMEA (Failure Mode and Effects Analysis) automáticamente a partir de los pasos de un proceso, utilizando la API de OpenAI.

[cc-by]: https://creativecommons.org/licenses/by/4.0/deed.es
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## 🌟 Características

- ✅ **Generación automática de FMEA** usando modelos avanzados de OpenAI (GPT-5.4, GPT-4o)
- 📊 **Análisis completo** con Severidad, Ocurrencia, Detección y cálculo automático de RPN
- 🎨 **Interfaz intuitiva** desarrollada con Streamlit
- ✏️ **Editor interactivo** para ajustar y refinar los resultados
- 📥 **Exportación a Excel** con formato profesional y colores condicionales
- 🌐 **Soporte multiidioma** (Español e Inglés)
- 🔧 **Altamente configurable** - número de modos de fallo, modelo de IA, etc.

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

4. **Configurar la API Key de OpenAI**
   
   Opción 1: Crear archivo `.env` (recomendado para desarrollo)
   ```bash
   copy .env.example .env
   ```
   Edita el archivo `.env` y agrega tu API key:
   ```
   OPENAI_API_KEY=tu-api-key-aqui
   ```
   
   Opción 2: Ingresar la API key directamente en la aplicación (recomendado para uso ocasional)

## ▶️ Uso

1. **Iniciar la aplicación**
   ```bash
   conda run -n fmea streamlit run app.py
   ```
   
   O si prefieres activar el ambiente primero:
   ```bash
   conda activate fmea
   streamlit run app.py
   ```

2. **En el navegador web**:
   - La aplicación se abrirá automáticamente en `http://localhost:8501`
   - Si no se abre, accede manualmente a esa URL

3. **Configuración inicial**:
   - Ingresa tu API Key de OpenAI en la barra lateral (o configúrala en archivo `.env`)
   - La aplicación usa el modelo **GPT-5.4** (modelo frontera de OpenAI)
   - Configura el número de modos de fallo por paso (2-3 recomendado)
   - Selecciona el idioma de salida (Español/English)

4. **Generar FMEA**:
   - Sube tu archivo Excel con los pasos del proceso
   - Haz clic en "Generar Análisis FMEA"
   - Espera mientras la IA analiza tu proceso
   - Revisa y edita los resultados en el editor interactivo
   - Descarga el análisis en Excel con formato profesional

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

- **API Key**: Ingrésala en la app o confígura archivo `.env` para desarrollo
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

- ⚠️ **No compartir API Keys**: Nunca subas archivos `.env` a repositorios públicos
- 🔐 **Datos del proceso**: Los datos se envían a OpenAI para el análisis. Revisa los términos de servicio de OpenAI
- 💾 **Datos locales**: La aplicación no almacena tus datos. Todo se procesa en memoria

## 💡 Consejos de Uso

1. **API Key**: Puedes ingresarla en la app o crear archivo `.env` con `OPENAI_API_KEY=tu-key`
2. **Procesos simples**: Usa 2 modos de fallo por paso para análisis rápidos y enfocados
3. **Procesos complejos**: Aumenta a 3-4 modos de fallo para análisis exhaustivos
4. **Edición**: Siempre revisa y ajusta los valores según tu experiencia del proceso
5. **Priorización**: Enfócate primero en items con RPN > 100

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
└── template_proceso.xlsx  # Ejemplo de archivo de entrada
```

## 🐛 Solución de Problemas

### Error: "Invalid API Key"
- Verifica que tu API key sea correcta (empieza con `sk-`)
- Asegúrate de tener créditos disponibles en tu cuenta de OpenAI
- Si usas archivo `.env`, verifica que esté en el directorio correcto

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
