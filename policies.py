"""Configurable evidence policy for vendor-neutral endpoint lifecycle."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Finding:
    stage: str
    control: str
    status: str
    severity: str

def evaluate_policy(policy: dict, evidence: dict) -> list[Finding]:
    """Policy: {stage: {control: 'high'|'medium'|'low'}}.
    Evidence: {stage: {control: True|False}}. Missing is not a pass.
    """
    if not isinstance(policy,dict) or not policy:
        raise ValueError("nonempty policy expected")
    findings=[]
    for stage,controls in policy.items():
        if not isinstance(controls,dict) or not controls:
            raise ValueError("each stage needs controls")
        records=evidence.get(stage,{})
        if not isinstance(records,dict):
            raise ValueError("stage evidence must be a mapping")
        for name,severity in controls.items():
            if severity not in ("high","medium","low"):
                raise ValueError("invalid severity")
            state=records.get(name,None)
            if state not in (True,False,None) or type(state) not in (bool,type(None)):
                raise ValueError("evidence must be true, false or null")
            findings.append(Finding(stage,name,
                "pass" if state is True else "fail" if state is False else "missing",
                severity))
    return findings

def summary(findings: list[Finding]) -> dict:
    return {"total":len(findings),
            "passed":sum(f.status=="pass" for f in findings),
            "high_priority_gaps":[f"{f.stage}.{f.control}" for f in findings
                                   if f.severity=="high" and f.status!="pass"]}
