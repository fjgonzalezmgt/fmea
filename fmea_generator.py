"""
Módulo para generar FMEA (Failure Mode and Effects Analysis) usando OpenAI API
"""
import pandas as pd
import json
from typing import List, Dict, Optional
from openai import OpenAI


class FMEAGenerator:
    """Generador de análisis FMEA usando IA"""
    
    def __init__(self, api_key: str, model: str = "gpt-5.4", language: str = "es"):
        """
        Inicializar el generador FMEA
        
        Args:
            api_key: API key de OpenAI
            model: Modelo a utilizar (gpt-5.4, gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-3.5-turbo)
            language: Idioma de salida ('es' o 'en')
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.language = language
        
    def read_process_excel(self, file) -> pd.DataFrame:
        """
        Leer archivo Excel con pasos del proceso
        
        Args:
            file: Archivo Excel (BytesIO o ruta)
            
        Returns:
            DataFrame con los pasos del proceso
        """
        try:
            df = pd.read_excel(file)
            return df
        except Exception as e:
            raise ValueError(f"Error al leer el archivo Excel: {str(e)}")
    
    def validate_process_data(self, df: pd.DataFrame) -> tuple[bool, str]:
        """
        Validar que el DataFrame tenga las columnas necesarias
        
        Args:
            df: DataFrame a validar
            
        Returns:
            Tupla (es_valido, mensaje_error)
        """
        # Columnas requeridas (al menos una de estas debe existir para descripción)
        required_cols = ['descripcion', 'descripción', 'description', 'nombre', 'nombre del paso', 'paso']
        
        # Verificar que exista al menos una columna de descripción
        has_description = any(col.lower() in [c.lower() for c in df.columns] for col in required_cols)
        
        if not has_description:
            return False, f"El Excel debe contener al menos una columna de descripción del paso. Columnas encontradas: {', '.join(df.columns)}"
        
        if len(df) == 0:
            return False, "El archivo Excel está vacío"
            
        return True, ""
    
    def get_description_column(self, df: pd.DataFrame) -> str:
        """Identificar la columna de descripción del proceso"""
        possible_names = ['descripcion', 'descripción', 'description', 'nombre', 'nombre del paso', 'paso', 'actividad']
        
        for col in df.columns:
            if col.lower() in possible_names:
                return col
                
        # Si no encuentra, usar la segunda columna (asumiendo que la primera es número)
        if len(df.columns) > 1:
            return df.columns[1]
        return df.columns[0]
    
    def get_step_info(self, row: pd.Series, desc_col: str) -> str:
        """Construir descripción completa del paso incluyendo toda la información disponible"""
        info_parts = []
        
        # Descripción principal
        info_parts.append(f"Paso: {row[desc_col]}")
        
        # Agregar otras columnas relevantes si existen
        optional_cols = {
            'responsable': 'Responsable',
            'entradas': 'Entradas',
            'entrada': 'Entradas',
            'salidas': 'Salidas',
            'salida': 'Salidas',
            'recursos': 'Recursos',
            'herramientas': 'Herramientas',
            'procedimiento': 'Procedimiento',
            'detalles': 'Detalles'
        }
        
        for col in row.index:
            col_lower = col.lower()
            if col_lower in optional_cols and pd.notna(row[col]) and str(row[col]).strip():
                info_parts.append(f"{optional_cols[col_lower]}: {row[col]}")
        
        return " | ".join(info_parts)
    
    def build_fmea_prompt(self, process_steps: List[str], num_failures: int = 2) -> str:
        """
        Construir el prompt para generar FMEA
        
        Args:
            process_steps: Lista de descripciones de pasos del proceso
            num_failures: Número de modos de fallo a generar por paso
            
        Returns:
            Prompt para OpenAI
        """
        if self.language == "es":
            prompt = f"""Eres un experto en análisis FMEA (Análisis de Modos de Fallo y Efectos). 

Analiza los siguientes pasos de un proceso y genera un análisis FMEA completo. Para cada paso del proceso, identifica {num_failures} modos de fallo potenciales diferentes.

ESCALAS A UTILIZAR:

**Severidad (S)** - Gravedad del efecto del fallo:
- 10: Peligroso sin advertencia
- 9: Peligroso con advertencia
- 8: Muy alta (producto inservible)
- 7: Alta (producto con degradación importante)
- 6: Moderada (producto con degradación moderada)
- 5: Baja (producto con degradación menor)
- 4: Muy baja (afecta apariencia o sonido)
- 3: Menor (defecto notado por cliente discriminante)
- 2: Muy menor (defecto no notado por cliente)
- 1: Ninguna (sin efecto)

**Ocurrencia (O)** - Probabilidad de que ocurra la causa:
- 10: Casi inevitable (≥1 en 2)
- 9: Muy alta (1 en 3)
- 8: Alta repetida (1 en 8)
- 7: Alta frecuente (1 en 20)
- 6: Moderada frecuente (1 en 80)
- 5: Moderada ocasional (1 en 400)
- 4: Moderada (1 en 2,000)
- 3: Baja (1 en 15,000)
- 2: Remota (1 en 150,000)
- 1: Casi imposible (≤1 en 1,500,000)

**Detección (D)** - Capacidad de detectar el fallo antes de llegar al cliente:
- 10: Imposible detección (sin control)
- 9: Muy remota (control probablemente inefectivo)
- 8: Remota (control poco efectivo)
- 7: Muy baja (control de baja efectividad)
- 6: Baja (control de cierta efectividad)
- 5: Moderada (control de efectividad moderada)
- 4: Moderadamente alta (control efectivo)
- 3: Alta (control altamente efectivo)
- 2: Muy alta (controles casi seguros)
- 1: Casi certeza (detección automática confiable)

PASOS DEL PROCESO:
{chr(10).join(f"{i+1}. {step}" for i, step in enumerate(process_steps))}

Genera un análisis FMEA completo en formato JSON con la siguiente estructura:
{{
  "fmea_items": [
    {{
      "numero_paso": 1,
      "paso_proceso": "descripción del paso",
      "modo_fallo": "descripción del modo de fallo potencial",
      "efecto_fallo": "consecuencias si ocurre el fallo",
      "severidad": 7,
      "causa_potencial": "por qué puede ocurrer",
      "ocurrencia": 5,
      "controles_actuales": "métodos de prevención/detección sugeridos",
      "deteccion": 4,
      "acciones_recomendadas": "mejoras sugeridas para reducir riesgo"
    }}
  ]
}}

IMPORTANTE:
- Genera exactamente {num_failures} modos de fallo diferentes para CADA paso del proceso
- Los valores de severidad, ocurrencia y detección deben ser números enteros entre 1 y 10
- Sé específico y realista en los modos de fallo y sus causas
- Adapta el análisis al tipo de proceso descrito
- Las respuestas deben ser concisas pero informativas
"""
        else:  # English
            prompt = f"""You are an expert in FMEA (Failure Mode and Effects Analysis).

Analyze the following process steps and generate a complete FMEA analysis. For each process step, identify {num_failures} different potential failure modes.

SCALES TO USE:

**Severity (S)** - Severity of the failure effect:
- 10: Hazardous without warning
- 9: Hazardous with warning
- 8: Very high (product unusable)
- 7: High (product with major degradation)
- 6: Moderate (product with moderate degradation)
- 5: Low (product with minor degradation)
- 4: Very low (affects appearance or sound)
- 3: Minor (defect noticed by discriminating customer)
- 2: Very minor (defect not noticed by customer)
- 1: None (no effect)

**Occurrence (O)** - Probability of the cause occurring:
- 10: Almost inevitable (≥1 in 2)
- 9: Very high (1 in 3)
- 8: Repeated high (1 in 8)
- 7: Frequent high (1 in 20)
- 6: Frequent moderate (1 in 80)
- 5: Occasional moderate (1 in 400)
- 4: Moderate (1 in 2,000)
- 3: Low (1 in 15,000)
- 2: Remote (1 in 150,000)
- 1: Almost impossible (≤1 in 1,500,000)

**Detection (D)** - Ability to detect the failure before reaching the customer:
- 10: Impossible detection (no control)
- 9: Very remote (probably ineffective control)
- 8: Remote (not very effective control)
- 7: Very low (low effectiveness control)
- 6: Low (some effectiveness control)
- 5: Moderate (moderate effectiveness control)
- 4: Moderately high (effective control)
- 3: High (highly effective control)
- 2: Very high (almost certain controls)
- 1: Almost certain (reliable automatic detection)

PROCESS STEPS:
{chr(10).join(f"{i+1}. {step}" for i, step in enumerate(process_steps))}

Generate a complete FMEA analysis in JSON format with the following structure:
{{
  "fmea_items": [
    {{
      "numero_paso": 1,
      "paso_proceso": "step description",
      "modo_fallo": "potential failure mode description",
      "efecto_fallo": "consequences if failure occurs",
      "severidad": 7,
      "causa_potencial": "why it may occur",
      "ocurrencia": 5,
      "controles_actuales": "suggested prevention/detection methods",
      "deteccion": 4,
      "acciones_recomendadas": "suggested improvements to reduce risk"
    }}
  ]
}}

IMPORTANT:
- Generate exactly {num_failures} different failure modes for EACH process step
- Severity, occurrence, and detection values must be integers between 1 and 10
- Be specific and realistic in failure modes and their causes
- Adapt the analysis to the type of process described
- Responses should be concise but informative
"""
        
        return prompt
    
    def generate_fmea(self, df: pd.DataFrame, num_failures: int = 2, progress_callback=None) -> pd.DataFrame:
        """
        Generar análisis FMEA completo
        
        Args:
            df: DataFrame con pasos del proceso
            num_failures: Número de modos de fallo por paso
            progress_callback: Función opcional para actualizar progreso
            
        Returns:
            DataFrame con el análisis FMEA
        """
        # Validar datos
        is_valid, error_msg = self.validate_process_data(df)
        if not is_valid:
            raise ValueError(error_msg)
        
        # Identificar columna de descripción
        desc_col = self.get_description_column(df)
        
        # Construir lista de pasos con toda la información
        process_steps = []
        for idx, row in df.iterrows():
            step_info = self.get_step_info(row, desc_col)
            process_steps.append(step_info)
        
        # Construir prompt
        prompt = self.build_fmea_prompt(process_steps, num_failures)
        
        if progress_callback:
            progress_callback(0.3, "Enviando solicitud a OpenAI...")
        
        # Llamar a OpenAI API
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Eres un experto en análisis FMEA y calidad de procesos. Siempre respondes en formato JSON válido."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.7
            )
            
            if progress_callback:
                progress_callback(0.7, "Procesando respuesta...")
            
            # Parsear respuesta
            result = json.loads(response.choices[0].message.content)
            
            # Convertir a DataFrame
            fmea_df = pd.DataFrame(result['fmea_items'])
            
            # Calcular RPN (Risk Priority Number)
            fmea_df['RPN'] = fmea_df['severidad'] * fmea_df['ocurrencia'] * fmea_df['deteccion']
            
            # Reordenar columnas
            column_order = [
                'numero_paso', 'paso_proceso', 'modo_fallo', 'efecto_fallo',
                'severidad', 'causa_potencial', 'ocurrencia', 'controles_actuales',
                'deteccion', 'RPN', 'acciones_recomendadas'
            ]
            
            # Solo reordenar las columnas que existen
            existing_cols = [col for col in column_order if col in fmea_df.columns]
            fmea_df = fmea_df[existing_cols]
            
            if progress_callback:
                progress_callback(1.0, "¡FMEA generado exitosamente!")
            
            return fmea_df
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al parsear la respuesta de OpenAI: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error al generar FMEA: {str(e)}")
    
    def export_to_excel(self, fmea_df: pd.DataFrame, output_file: str):
        """
        Exportar FMEA a Excel con formato
        
        Args:
            fmea_df: DataFrame con FMEA
            output_file: Ruta del archivo de salida
        """
        from openpyxl import load_workbook
        from openpyxl.styles import Font, PatternFill, Alignment
        from openpyxl.utils import get_column_letter
        
        # Exportar a Excel
        fmea_df.to_excel(output_file, index=False, sheet_name='FMEA')
        
        # Cargar workbook para aplicar formato
        wb = load_workbook(output_file)
        ws = wb['FMEA']
        
        # Formato de encabezados
        header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
        header_font = Font(bold=True, color="FFFFFF", size=11)
        
        for cell in ws[1]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
        # Formato condicional para RPN
        rpn_col_idx = None
        for idx, col in enumerate(fmea_df.columns, 1):
            if col == 'RPN':
                rpn_col_idx = idx
                break
        
        if rpn_col_idx:
            col_letter = get_column_letter(rpn_col_idx)
            
            # Verde para RPN < 50
            green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
            # Amarillo para RPN 50-100
            yellow_fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
            # Rojo para RPN > 100
            red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
            
            for row_idx in range(2, len(fmea_df) + 2):
                cell = ws[f"{col_letter}{row_idx}"]
                rpn_value = cell.value
                
                if rpn_value is not None:
                    if rpn_value > 100:
                        cell.fill = red_fill
                    elif rpn_value >= 50:
                        cell.fill = yellow_fill
                    else:
                        cell.fill = green_fill
        
        # Ajustar ancho de columnas
        for column in ws.columns:
            max_length = 0
            column_letter = get_column_letter(column[0].column)
            
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            
            adjusted_width = min(max_length + 2, 50)
            ws.column_dimensions[column_letter].width = adjusted_width
        
        # Habilitar filtros
        ws.auto_filter.ref = ws.dimensions
        
        # Guardar
        wb.save(output_file)
