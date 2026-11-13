# Endpoint lifecycle reference workflow

Vendor-neutral training illustration, not an employer-approved standard operating procedure.

```mermaid
flowchart TD
  A[Device request] --> B{Business owner and approval evidence?}
  B -- No --> X[Record evidence gap]
  B -- Yes --> C[Provision and enroll]
  C --> D{Asset tag and enrollment verified?}
  D -- No --> X
  D -- Yes --> E[Secure baseline]
  E --> F{Encryption and patch evidence?}
  F -- No --> X
  F -- Yes --> G[Operate and support]
  G --> H{Named support owner and monitoring?}
  H -- No --> X
  H -- Yes --> I[Retire device]
  I --> J{Wipe evidence and inventory updated?}
  J -- No --> X
  J -- Yes --> K[Lifecycle complete]
  X --> L[Remediate and revalidate]
```

The public `app.py` evaluates required evidence flags by lifecycle stage; the diagram expresses the intended review sequence. It is not a substitute for endpoint security, compliance, retention or hardware lifecycle requirements.

Run `python cli.py examples/sample_evidence.json` for a fictional complete record.
