# Teams Calling Cutover Lab

A 20-minute tabletop for a voice lead, test caller, and service desk lead. All events are fictional. Use the evidence below to decide which migration waves can proceed.

## Briefing

Two appointment offices share a receptionist. Wave A moved yesterday. Wave B moved this morning. A third wave is scheduled in 15 minutes. Both offices require external callers to reach the correct receptionist. In this exercise a previously tested alternate line is available for each office.

| Test at 09:05 | Office A | Office B |
| --- | --- | --- |
| External caller to published number | Correct receptionist | Call disconnects |
| Staff member to external test contact | Connected | Connected |
| Internal extension to receptionist | Connected | Connected |
| Second external caller on another carrier | Correct receptionist | Call disconnects |

**Decision 1.** Which users are affected? Which tests tell you that? Assign someone to protect inbound access, someone to investigate the failed path, and someone to update the desk. Decide what happens to wave three.

<details><summary>Reveal the 09:12 update after making your decision</summary>

The voice lead finds that office B's published range still points to the old destination. The service desk confirms that a test caller reached B through the alternate line. A routing correction is reported complete at 09:18.

**Decision 2.** Decide what evidence would justify restoring normal service, removing the fallback, and starting another wave. Record the decision, owner, time, and outstanding risks.

</details>

<details><summary>Facilitator debrief</summary>

Hold the next wave. Preserve working service in A. Confirm B's alternate path with an external caller and give the desk a time for the next update. Outbound success says little about the inbound route. Two failed external tests narrow the investigation but do not alone establish the cause.

After correction, repeat external inbound tests for B from both origins, confirm the intended recipient answers, and repeat A as a control. Check outbound and internal calling for regressions. Retain the fallback until the voice lead and office contact accept the results. If inbound tests still fail, keep the fallback and the hold in place. Resuming the rollout is a separate decision.

</details>

| Time | Decision | Evidence | Owner | Next check |
| --- | --- | --- | --- | --- |
| 09:05 | | | | |
| 09:12 | | | | |
| 09:18 | | | | |
