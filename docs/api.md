# Numnio API Reference

Base URL: `https://api.numnio.dev`

All requests require a bearer token:

```
Authorization: Bearer $NUMNIO_API_KEY
```

## Inspect

### `POST /v1/inspect/jobs`

Start an inspection job on a production line.

```json
{
  "line": "line1",
  "model": "visualinspect-v2",
  "output": {"mode": "defects", "schema": "v1"}
}
```

Response:

```json
{
  "job_id": "job_8f3a...",
  "status": "running"
}
```

### `GET /v1/inspect/jobs/:id`

Poll job status and results. Completed jobs return defect records:

```json
{
  "job_id": "job_8f3a...",
  "status": "succeeded",
  "defects": [
    {
      "type": "solder_bridge",
      "severity": "major",
      "confidence": 0.97,
      "cause": "Insufficient solder paste on pad 14; consistent with stencil clogging.",
      "action": "Clean stencil, re-run pad 14 AOI sample."
    }
  ]
}
```

## Maintenance

### `GET /v1/maintenance/anomalies`

Returns the PredictOps anomaly feed:

```json
{
  "anomalies": [
    {
      "machine": "press_02",
      "signal": "vibration_rms",
      "value": 4.8,
      "baseline": 2.1,
      "unit": "mm/s",
      "status": "open"
    }
  ]
}
```

### `POST /v1/maintenance/briefs`

Generate a maintenance brief for an anomaly with Claude reasoning:

```json
{"anomaly_id": "an_92c1..."}
```

## Yield

### `POST /v1/yield/optimize`

Request setpoint recommendations for a line:

```json
{
  "line": "line1",
  "objective": "maximize_yield",
  "constraints": {"max_temp_c": 240}
}
```

Response includes suggestions with rationale:

```json
{
  "suggestions": [
    {
      "parameter": "zone3_temp_c",
      "current": 232,
      "suggested": 235,
      "expected_yield_delta": "+1.8%",
      "rationale": "Zone 3 has been running 4°C below the historical optimum for the current material lot."
    }
  ]
}
```

## Copilot

### `POST /v1/copilot/ask`

Operator copilot endpoint (Claude agent with scoped tool access):

```json
{
  "question": "Why did line1 yield drop this morning?",
  "scope": ["mes", "inspect", "maintenance"]
}
```

---

Contact: visualfeed@numnio.dev
