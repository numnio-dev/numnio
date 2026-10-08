# Numnio

**AI copilots for manufacturing — built on Claude.**

Numnio turns shop-floor cameras and machine telemetry into operator-ready decisions: zero-defect visual inspection, predictive maintenance, and real-time yield optimization.

Website: https://numnio.dev

---

## What's in this repo

| Path | Description |
|---|---|
| `examples/inspect_example.py` | Call the Numnio inspection API and parse defect results |
| `examples/claude_analyze.py` | Direct Claude API example used for root-cause analysis prompts |
| `examples/requirements.txt` | Python dependencies |
| `docs/api.md` | API reference (inspection, maintenance, yield) |

## Why Claude

Numnio uses the Claude API as its reasoning core:

- **Vision** — defect classification and explanation on escalated inspection frames
- **Reasoning** — root-cause analysis across telemetry, logs, and manuals
- **Tool use** — operator copilot that queries MES/CMMS with scoped permissions
- **Batch API** — nightly factory-wide drift and trend analysis

## Quickstart

```bash
pip install -r examples/requirements.txt
export NUMNIO_API_KEY=...
export ANTHROPIC_API_KEY=...

python examples/inspect_example.py   # runs a sample inspection job
python examples/claude_analyze.py    # runs a root-cause analysis prompt on Claude
```

## Architecture

```
Edge (camera / PLC / sensors)
      │  MQTT / OPC-UA
      ▼
Numnio Stream Processor  ── frames, windows, events
      │
      ▼
Claude API Layer
   ├─ Vision analysis (defect classification)
   ├─ Reasoning (root cause, maintenance briefs)
   ├─ Tool use (MES queries, manual lookup)
   └─ Batch API (nightly factory-wide analytics)
      │  validated JSON
      ▼
Factory systems: MES / SCADA / CMMS / dashboards
```

## Contact

visualfeed@numnio.dev
