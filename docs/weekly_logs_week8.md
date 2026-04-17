\# Week 8 Log – Predictive Urban Infrastructure Management



\## Goals

\- Extend the project with reinforcement learning

\- Compare RL against the fixed-time baseline

\- Improve the RL controller through targeted tuning

\- Add a rerouting incident scenario with true road closure

\- Integrate new results into the dashboard



\## Work Completed



\### 1. Reinforcement Learning controller

\- Implemented a Q-learning traffic signal controller

\- Built RL state, action, and reward structure using live SUMO traffic data

\- Trained the RL agent over multiple episodes

\- Evaluated RL on the medium scenario

\- Compared original and improved RL behaviour against the baseline



\### 2. RL performance comparison

\- Generated summary metrics for:

&#x20; - baseline medium

&#x20; - original RL medium

&#x20; - improved RL medium

\- Produced an RL comparison plot showing average waiting time

\- Confirmed that the RL system functions correctly even though the baseline remained stronger



\### 3. Incident reroute scenario

\- Implemented a true road-closure incident rather than simple slowdown

\- Added rerouting logic for affected vehicles

\- Tuned the incident activation window to maintain simulation stability

\- Generated outputs for the reroute experiment

\- Compared reroute incident performance with existing incident cases



\### 4. Dashboard updates

\- Updated Streamlit dashboard text to include RL mode

\- Added RL analysis support

\- Updated incident section to include the reroute run



\---



\## Evidence

\- `src/rl/rl\_utils.py`

\- `src/rl/train\_q\_learning.py`

\- `src/rl/evaluate\_q\_learning.py`

\- `src/control/incident\_reroute\_controller.py`

\- `src/evaluation/compare\_medium\_rl\_check.py`

\- `src/evaluation/compare\_incident\_reroute.py`

\- `results/medium\_rl\_check\_summary.csv`

\- `results/plots/medium\_rl\_check\_waiting\_time.png`

\- `results/incident\_reroute\_summary.csv`

\- `results/plots/incident\_reroute\_waiting\_time\_comparison.png`

\- updated `src/dashboard/app.py`



\---



\## Key Observations

\- The RL controller was successfully integrated into the project as an advanced AI extension

\- The fixed-time baseline still outperformed RL on the medium scenario

\- RL tuning changed performance but did not surpass the baseline

\- This result is still useful because it supports critical evaluation of AI complexity versus traditional control

\- The incident reroute scenario adds a more realistic disruption case to the project



\---



\## Interpretation

Week 8 strengthened the project by adding a more advanced AI method and a more realistic disruption scenario. Although RL did not outperform the fixed-time baseline, it provided valuable experimental evidence and made the final project more sophisticated from both a technical and evaluation perspective.



\---



\## Next Steps

\- finalise experiment summaries and plots

\- polish dashboard and visuals

\- write final report sections for results, discussion, conclusion, and future work

\- prepare final demo and presentation

