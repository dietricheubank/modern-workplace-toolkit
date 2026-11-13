"""Run a generalized endpoint lifecycle checklist from JSON evidence."""
import argparse
import json
from pathlib import Path
from app import report, STAGES, validate

def main():
    parser = argparse.ArgumentParser(description="Check evidence for endpoint lifecycle controls")
    parser.add_argument("evidence", help="Path to a JSON map of lifecycle-stage evidence")
    args = parser.parse_args()
    data = json.loads(Path(args.evidence).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object")
    print(report(data))
    return 0 if all(validate(stage, data.get(stage, {})).passed for stage in STAGES) else 1

if __name__ == "__main__":
    raise SystemExit(main())
