\# Week 9 Log – Predictive Urban Infrastructure Management



\## Goals

\- Extend the project with a hierarchical RL architecture

\- Introduce both global and local RL control layers

\- Evaluate whether a coordinated RL structure improves on earlier RL results

\- Prepare final advanced AI extension for inclusion in report and demo



\## Work Completed



\### 1. Hierarchical RL design

\- Implemented a two-level reinforcement learning architecture

\- Added:

&#x20; - one global RL agent for network-wide coordination

&#x20; - one shared local RL agent for junction-level control

\- Used `global\_mode` as the coordination signal between levels



\### 2. Training setup

\- Built a new training script for hierarchical Q-learning

\- Trained both global and local Q-tables simultaneously

\- Stored reward data for learning-curve analysis



\### 3. Evaluation

\- Evaluated hierarchical RL on the medium traffic scenario

\- Generated output trip information for comparison

\- Compared:

&#x20; - baseline medium

&#x20; - original RL medium

&#x20; - improved RL medium

&#x20; - hierarchical RL medium



\### 4. Project impact

\- Added a more sophisticated AI control architecture

\- Strengthened the final report discussion by showing progression from:

&#x20; - fixed baseline

&#x20; - predictive ML control

&#x20; - single-agent RL

&#x20; - hierarchical RL



\## Evidence

\- `src/rl/hierarchical\_utils.py`

\- `src/rl/train\_hierarchical\_q\_learning.py`

\- `src/rl/evaluate\_hierarchical\_q\_learning.py`

\- `src/evaluation/compare\_hierarchical\_rl\_medium.py`

\- `results/rl/global\_q\_table.npy`

\- `results/rl/local\_q\_table.npy`

\- `results/rl/hierarchical\_training\_rewards.csv`

\- `results/rl/hierarchical\_training\_rewards.png`

\- `results/hierarchical\_rl\_medium\_summary.csv`



\## Key Observations

\- The hierarchical structure is more expressive than the previous single-agent RL setup

\- It better reflects realistic traffic-management architecture by separating global coordination from local control

\- Even if it does not outperform the fixed-time baseline, it significantly strengthens the technical sophistication of the project



\## Interpretation

Week 9 serves as an advanced AI extension phase. The hierarchical RL design improves the conceptual strength of the system and provides a strong basis for discussion of multi-level decision-making in predictive urban infrastructure management.



\## Next Steps

\- final code cleanup

\- final dashboard/report screenshot collection

\- final report writing

\- final presentation/demo preparation

