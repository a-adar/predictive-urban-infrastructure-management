\# Week 6 Log – Predictive Urban Infrastructure Management



\## Goals

\- Add an incident handling scenario

\- Test system robustness under disruption

\- Compare AI vs baseline performance during the incident

\- Produce results for recovery-focused evaluation



\## Work Completed

\- Generated a denser traffic scenario to represent an incident-style demand surge

\- Created a dedicated incident SUMO configuration

\- Ran the fixed-time baseline under the incident

\- Ran the AI adaptive controller under the incident

\- Parsed outputs into CSV

\- Compared systems using average waiting time, trip duration, time loss, and throughput-style measures



\## Evidence

\- `simulation/routes/chicago\_incident.rou.xml`

\- `simulation/configs/chicago\_incident.sumocfg`

\- `results/tripinfo\_incident\_baseline.csv`

\- `results/tripinfo\_incident\_ai.csv`

\- `results/incident\_summary.csv`

\- `results/plots/incident\_waiting\_time\_comparison.png`



\## Observations

\- The system now includes a stress-testing scenario aligned with the project brief

\- The incident experiment provides evidence of robustness and disruption response

\- Results can now be used to discuss the strengths and limitations of the AI controller under dynamic demand



\## Next Steps

\- final experiment cleanup

\- additional graphs/tables

\- final report writing and demo preparation

