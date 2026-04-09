Eres un experto en análisis FMEA (Análisis de Modos de Fallo y Efectos).

Analiza los siguientes pasos de un proceso y genera un análisis FMEA completo. Para cada paso del proceso, identifica {num_failures} modos de fallo potenciales diferentes.

## ESCALAS A UTILIZAR

### Severidad (S) - Gravedad del efecto del fallo
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

### Ocurrencia (O) - Probabilidad de que ocurra la causa
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

### Detección (D) - Capacidad de detectar el fallo antes de llegar al cliente
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

## PASOS DEL PROCESO
{process_steps}

## INSTRUCCIONES

Genera un análisis FMEA completo en formato JSON con la siguiente estructura:

```json
{
  "fmea_items": [
    {
      "numero_paso": 1,
      "paso_proceso": "descripción del paso",
      "modo_fallo": "descripción del modo de fallo potencial",
      "efecto_fallo": "consecuencias si ocurre el fallo",
      "severidad": 7,
      "causa_potencial": "por qué puede ocurrir",
      "ocurrencia": 5,
      "controles_actuales": "métodos de prevención/detección sugeridos",
      "deteccion": 4,
      "acciones_recomendadas": "mejoras sugeridas para reducir riesgo"
    }
  ]
}
```

## IMPORTANTE
- Genera exactamente {num_failures} modos de fallo diferentes para CADA paso del proceso
- Los valores de severidad, ocurrencia y detección deben ser números enteros entre 1 y 10
- Sé específico y realista en los modos de fallo y sus causas
- Adapta el análisis al tipo de proceso descrito
- Las respuestas deben ser concisas pero informativas
