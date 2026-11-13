# Modern Workplace Toolkit

Vendor-neutral endpoint lifecycle policy validation and evidence checklist generator.

## Run

Requires Python 3.11+ and no third-party dependencies.

```bash
cd modern-workplace-toolkit
python app.py
python -m unittest discover -s tests -v
```

## Design / scope

This is an **independent starter project** staged under the public portfolio repository until a matching standalone GitHub repository can be created. The implementation is synthetic by default; no integrations with private systems, employer APIs, secrets, or confidential data.

Evidence checks are educational and must be adapted to approved policies, device classes, security requirements, and jurisdictional obligations.

## Next steps

- Extend coverage for invalid input and edge cases.
- Document real-world threat models, operational constraints, and test fixtures.
- Publish a dedicated repository without exposing private configurations.
- Add versioned sample data, user-facing CLI, and packaging when project grows.

License: MIT (parent repository).


## Repository status

This is the standalone public project. It is developed independently with GitHub Actions CI.

## Evidence checklist runner

```bash
python cli.py examples/sample_evidence.json
```

The CLI prints PASS or GAPS for each of five stages—request, provision, secure, operate, and retire. Its exit status is 0 only if all required evidence flags are true; otherwise 1. All example evidence is synthetic. The checklist is not a substitute for approved organizational security policies, asset management, records retention, or regulatory requirements.

**Development:** `python -m unittest discover -s tests -v`. CI runs the suite on each push and pull request.

## Configurable evidence policy engine

The [policy module](policies.py) evaluates custom stage-and-control requirements, distinguishing `pass`, `fail`, and `missing`, with high/medium/low severity. Unlike basic yes/no checks, absent evidence cannot silently pass. See [policy tests](tests/test_policies.py).

This is a public sample policy mechanism, not a substitute for organizational baseline standards, device telemetry or authoritative compliance assessment.
