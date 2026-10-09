# Numnio

**AI copilots for manufacturing — built with Claude.**

Numnio turns shop-floor cameras and machine telemetry into operator-ready decisions: zero-defect visual inspection, predictive maintenance, and real-time yield optimization.

Website: https://numnio.dev

---

## What's in this repo

| Path | Description |
|---|---|
| `examples/inspect_example.py` | Call the Numnio inspection API and parse defect results |
| `examples/requirements.txt` | Python dependencies |
| `docs/api.md` | API reference (inspection, maintenance, yield) |

## How we use Claude

Numnio is developed with Claude — from first prototype to production. Our team relies on Claude across the development workflow:

- **Claude Code** — writing, reviewing, and refactoring the platform's code and ML pipelines
- **Design assistance** — system architecture and data pipeline design; trade-off analysis
- **Docs & testing** — drafting API docs, test plans, and specs
- **Prototyping** — fast experiments and proofs of concept

## Quickstart

```bash
pip install -r examples/requirements.txt
export NUMNIO_API_KEY=...

python examples/inspect_example.py   # runs a sample inspection job
```

## Architecture

```
Edge (camera / PLC / sensors)
      │  MQTT / OPC-UA
      ▼
Numnio Stream Processor  ── frames, windows, events
      │
      ▼
Numnio AI Layer
   ├─ Vision analysis (defect classification)
   ├─ Reasoning (root cause, maintenance briefs)
   ├─ Tool use (MES queries, manual lookup)
   └─ Batch analytics (nightly factory-wide)
      │  validated JSON
      ▼
Factory systems: MES / SCADA / CMMS / dashboards
```

## Contact

visualfeed@numnio.dev
