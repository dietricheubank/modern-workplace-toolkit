# Clinical Workstation Performance Lab

This observer-operated Windows exercise measures elapsed time from the start of a simulated sign-in workflow to desktop visibility and then to completion of a fictional application task. Use a test workstation and a dummy application. The observer starts the timer on a second device so the timer survives sign-in. Human reaction time is part of the measurement.

Run from this folder with Python 3.11 or later:

    python measure.py clinic
    python measure.py care

At the first prompt, press Enter as the tester starts the workflow. At the second, mark the first usable desktop. At the third, mark the same predefined task every time, such as opening a fictional appointment and selecting an enabled button. Ctrl+C cancels an incomplete trial. Completed trials append to trials.csv in the current directory. Output includes the median and slowest total for the selected station type. Keep separate folders for different test conditions.

Run at least five trials per configuration with the same operator, application task, and initial session state. Measure fresh sign-in and unlock separately. A long desktop-to-task interval is a reason to investigate app readiness. It cannot by itself identify the cause. No patient records, device identifiers, or credentials are collected.
