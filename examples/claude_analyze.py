"""Root-cause analysis with the Claude API.

This is the pattern Numnio uses to turn raw alerts into operator-ready
maintenance briefs: feed Claude the anomaly context plus recent telemetry
and ask for a structured JSON brief.

Requires:
    ANTHROPIC_API_KEY environment variable
"""

import json
import os

import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

SYSTEM_PROMPT = """You are Numnio's maintenance reasoning engine for factory equipment.
Given an anomaly alert and recent telemetry, produce a maintenance brief.

Respond with ONLY a JSON object with these keys:
- likely_component: the component most likely failing
- confidence: 0.0-1.0
- evidence: array of short strings citing the telemetry signals
- suggested_action: one actionable sentence for the maintenance team
- urgency: one of "low", "medium", "high"
"""


def analyze_anomaly(alert: dict, telemetry: list[dict]) -> dict:
    """Ask Claude for a structured maintenance brief."""
    user_content = json.dumps({"alert": alert, "telemetry": telemetry}, indent=2)

    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_content}],
    )

    text = message.content[0].text
    return json.loads(text)


def main() -> None:
    alert = {
        "machine": "press_02",
        "signal": "vibration_rms",
        "value": 4.8,
        "baseline": 2.1,
        "unit": "mm/s",
        "window": "5m",
    }
    telemetry = [
        {"t": "T-10m", "vibration_rms": 2.2, "temp_c": 61.0, "current_a": 118},
        {"t": "T-5m", "vibration_rms": 3.1, "temp_c": 63.5, "current_a": 121},
        {"t": "T-2m", "vibration_rms": 4.1, "temp_c": 66.2, "current_a": 124},
        {"t": "now", "vibration_rms": 4.8, "temp_c": 68.9, "current_a": 127},
    ]

    brief = analyze_anomaly(alert, telemetry)
    print(json.dumps(brief, indent=2))


if __name__ == "__main__":
    main()
