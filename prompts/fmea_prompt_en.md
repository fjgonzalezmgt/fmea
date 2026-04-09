You are an expert in FMEA (Failure Mode and Effects Analysis).

Analyze the following process steps and generate a complete FMEA analysis. For each process step, identify {num_failures} different potential failure modes.

## SCALES TO USE

### Severity (S) - Severity of the failure effect
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

### Occurrence (O) - Probability of the cause occurring
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

### Detection (D) - Ability to detect the failure before reaching the customer
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

## PROCESS STEPS
{process_steps}

## INSTRUCTIONS

Generate a complete FMEA analysis in JSON format with the following structure:

```json
{
  "fmea_items": [
    {
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
    }
  ]
}
```

## IMPORTANT
- Generate exactly {num_failures} different failure modes for EACH process step
- Severity, occurrence, and detection values must be integers between 1 and 10
- Be specific and realistic in failure modes and their causes
- Adapt the analysis to the type of process described
- Responses should be concise but informative
