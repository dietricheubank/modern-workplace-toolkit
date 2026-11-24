# Modern Workplace Toolkit

Vendor-neutral endpoint lifecycle policy validation and evidence checklist generator.

## Workplace labs

- [Teams Calling Cutover Lab](labs/teams-calling-cutover/) — lead a fictional voice migration through an inbound calling failure.
- [Clinical Workstation Performance Lab](labs/clinical-workstation-performance/) — measure sign-in, desktop visibility, and application readiness.

## Run

Requires Python 3.11+ and no third-party dependencies.

```bash
cd modern-workplace-toolkit
python app.py
python -m unittest discover -s tests -v
```

## Design / scope

This standalone public project includes a Python implementation, a JSON command-line runner, synthetic examples, and automated checks in GitHub Actions.

Evidence checks are educational and must be adapted to approved policies, device classes, security requirements, and jurisdictional obligations.

## License

[MIT](LICENSE).

## Evidence checklist runner

```bash
python cli.py examples/sample_evidence.json
```

The CLI prints PASS or GAPS for each of five stages—request, provision, secure, operate, and retire. Its exit status is 0 only if all required evidence flags are true; otherwise 1. All example evidence is synthetic. The checklist is not a substitute for approved organizational security policies, asset management, records retention, or regulatory requirements.

**Development:** `python -m unittest discover -s tests -v`. CI runs the suite on each push and pull request.

## Configurable evidence policy engine

The [policy module](policies.py) evaluates custom stage-and-control requirements, distinguishing `pass`, `fail`, and `missing`, with high/medium/low severity. Unlike basic yes/no checks, absent evidence cannot silently pass. See [policy tests](tests/test_policies.py).

This is a public sample policy mechanism, not a substitute for organizational baseline standards, device telemetry or authoritative compliance assessment.
