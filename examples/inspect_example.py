"""Numnio inspection API example.

Runs a sample inspection job and prints defect results.

Requires:
    NUMNIO_API_KEY environment variable
"""

import json
import os
import time

import requests

API_BASE = os.environ.get("NUMNIO_API_BASE", "https://api.numnio.dev")


def start_inspection(line: str, model: str = "visualinspect-v2") -> dict:
    """Start an inspection job on a production line."""
    resp = requests.post(
        f"{API_BASE}/v1/inspect/jobs",
        headers={"Authorization": f"Bearer {os.environ['NUMNIO_API_KEY']}"},
        json={
            "line": line,
            "model": model,
            "output": {"mode": "defects", "schema": "v1"},
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def wait_for_job(job_id: str, timeout_s: int = 120) -> dict:
    """Poll until the job completes and return its results."""
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        resp = requests.get(
            f"{API_BASE}/v1/inspect/jobs/{job_id}",
            headers={"Authorization": f"Bearer {os.environ['NUMNIO_API_KEY']}"},
            timeout=30,
        )
        resp.raise_for_status()
        job = resp.json()
        if job["status"] in ("succeeded", "failed"):
            return job
        time.sleep(2)
    raise TimeoutError(f"job {job_id} did not finish within {timeout_s}s")


def main() -> None:
    job = start_inspection("line1")
    print(f"started job: {job['job_id']}")

    result = wait_for_job(job["job_id"])
    print(json.dumps(result, indent=2))

    for defect in result.get("defects", []):
        print(
            f"[{defect['severity']:>5}] {defect['type']} "
            f"({defect['confidence']:.0%}) — {defect['cause']}"
        )
        print(f"        action: {defect['action']}")


if __name__ == "__main__":
    main()
