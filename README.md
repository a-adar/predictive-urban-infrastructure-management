# AI-Driven Predictive Traffic Signal Management



## Project Overview



This project focuses on predictive urban infrastructure management using traffic systems as a case study. The system models a small real-world urban road network and applies data-driven techniques to improve traffic flow through predictive and adaptive control.



The core idea is to use simulation data to forecast short-term congestion and dynamically adjust traffic signal behaviour to improve efficiency compared to traditional fixed-time systems.



---



## Objectives



- Build a realistic urban traffic simulation using SUMO

- Collect time-series traffic data from the simulation

- Develop a predictive model for short-term congestion

- Implement an adaptive traffic signal controller

- Compare performance against a fixed-time baseline system

- Evaluate performance under different traffic conditions



---



## System Architecture



The system consists of the following components:



1\. Traffic Simulation (SUMO)

2\. Data Collection (traffic metrics logging)

3\. Forecasting Model (machine learning)

4\. Adaptive Controller (signal optimisation)

5\. Evaluation Module (performance comparison)



---



## Week 1 Progress



During Week 1, the focus was on project planning, system design, and environment setup.



### Completed Tasks



- Defined project scope (traffic-based smart infrastructure system)

- Selected simulation-based approach using SUMO

- Designed system architecture (simulation → data → prediction → control)

- Defined baseline system (fixed-time traffic signals)

- Identified key evaluation metrics:

&#x20; - average waiting time

&#x20; - queue length

&#x20; - travel time

&#x20; - throughput

- Created project folder structure

- Set up Python environment and required libraries

- Installed and configured SUMO

- Drafted initial project specification



### Key Decisions



- Focus on traffic signal optimisation rather than full smart-city system

- Use a small, controlled road network for experimentation

- Use simulation-generated data instead of external datasets

- Start with a fixed-time baseline before introducing AI



---



## Week 2 Progress





- Imported real-world Chicago road network

- Built working SUMO simulation

- Generated multiple traffic scenarios

- Logged simulation outputs

- Converted XML data to CSV

- Produced baseline performance metrics and plots



---

## Week 3 Progress

During Week 3, the project transitioned from a simulation-based system to an AI-driven predictive system by developing a machine learning model using the generated traffic data.

### Dataset Construction

- Combined simulation outputs from multiple traffic scenarios:
  - low traffic
  - medium traffic
  - high traffic
- Extracted key features from SUMO outputs (`tripinfo.xml` → CSV):
  - route length
  - travel duration
  - waiting time
- Created a unified dataset (`dataset.csv`) for machine learning

---

### Prediction Task Definition

- Defined the prediction goal as:
  
  **Predict vehicle waiting time based on traffic conditions**

- Selected features:
  - route length
  - travel duration
  - traffic scenario (low, medium, high)

- Target variable:
  - waiting time

---

### Machine Learning Model

- Implemented a baseline model using Linear Regression
- Split dataset into training and testing sets
- Trained model to predict waiting time from input features

---

### Evaluation

- Evaluated model performance using Mean Absolute Error (MAE)
- Generated prediction vs actual plots to visualise accuracy

---

### Key Result

- Successfully built a working predictive model for traffic waiting time
- Model captures general trends in congestion behaviour across different traffic scenarios

---

### Project Progress Summary

At this stage, the system includes:

- A real-world traffic simulation (Chicago road network)
- Multiple traffic scenarios (low, medium, high)
- A fixed-time baseline system
- Data extraction and processing pipeline
- A working machine learning model for traffic prediction

---

### Next Steps

- Improve prediction model (e.g., more features or advanced models)
- Integrate predictions into traffic signal control logic
- Develop adaptive traffic management system
- Compare AI-driven system against baseline performance


---

## Week 4 Progress

During Week 4, the project evolved into a fully integrated AI-driven system by connecting the prediction model to real-time traffic control within the SUMO simulation.

---

### Adaptive Traffic Control System

- Implemented a real-time controller using TraCI (SUMO control interface)
- Extracted live traffic data from simulation:
  - average waiting time across lanes
  - dynamic congestion state
- Integrated trained ML model (`model.pkl`) into simulation loop
- Generated real-time predictions of traffic congestion

---

### AI-Based Control Logic

- Designed a rule-based adaptive controller driven by ML predictions
- Control strategy:
  - If predicted waiting time is high → extend green phase duration
  - If predicted waiting time is low → maintain normal timing
- Introduced control interval to stabilise system behaviour
- Implemented mode switching:
  - NORMAL mode (standard timings)
  - CONGESTED mode (extended green phases)

---

### System Integration

- Built a closed-loop system:
Simulation → Data Extraction → ML Prediction → Traffic Control → Updated Simulation


- Ensured real-time interaction between simulation and AI controller
- Verified that traffic signal behaviour changes dynamically based on predicted congestion

---

### AI System Output

- Ran simulation using adaptive controller
- Generated AI-controlled output:
- `tripinfo_ai.xml`
- `edge_data_ai.xml`
- Converted outputs into CSV for analysis:
- `tripinfo_ai.csv`

---

### Performance Results

Baseline (Medium Traffic):
- Vehicles completed: 1607
- Average waiting time: ~164.23
- Average time loss: ~217.34

AI-Controlled System:
- Vehicles completed: 1582
- Average waiting time: ~202.93
- Average time loss: ~261.63

---

### Observations

- The AI controller successfully modifies traffic signal behaviour in response to predicted congestion
- The system demonstrates a fully functional AI-driven control loop
- However, performance did not improve compared to baseline in the current configuration
- This suggests:
- limitations in feature representation
- simplistic control logic
- need for further optimisation

---

### Key Achievements

- Successfully integrated machine learning model into live simulation
- Developed a real-time adaptive traffic signal controller
- Built a complete AI-driven infrastructure system
- Generated measurable outputs for AI vs baseline comparison

---

### Relation to Project Objectives

This stage satisfies key project requirements:

- Time-series prediction for demand estimation
- Real-time system optimisation using AI
- Integration of AI with a complex simulation environment
- Generation of before-vs-after performance metrics for evaluation :contentReference[oaicite:0]{index=0}

---

### Next Steps

- Improve prediction model (feature engineering, better models)
- Refine control strategy (more granular signal control)
- Conduct systematic evaluation across scenarios
- Perform ablation studies to isolate AI impact
- Analyse system stability and robustness


---

## Week 5 Progress

During Week 5, the project focused on improving and evaluating the AI-driven traffic controller through controlled experiments across multiple traffic scenarios.

### Controller Improvements

- Replaced binary phase-duration control with smoother proportional adjustment
- Added vehicle count as an additional live feature for the prediction pipeline
- Retrained the machine learning model to support the updated feature set
- Improved the stability of the real-time controller

### Experimental Evaluation

- Ran AI-controlled simulations for:
  - low traffic
  - medium traffic
  - high traffic
- Saved AI outputs separately for each scenario
- Converted simulation outputs from XML to CSV
- Compared AI performance directly against the fixed-time baseline

### Evaluation Metrics

The following metrics were used for comparison:
- average waiting time
- average trip duration
- average time loss
- total vehicles completed

### Key Outcome

The project now includes a full experimental pipeline:

Simulation → Data Extraction → Prediction → Adaptive Control → Evaluation

This allows direct measurement of the effect of the AI controller relative to the baseline system.

### Next Steps

- analyse strengths and limitations of the AI controller
- refine feature engineering and control thresholds
- write final report sections for results, discussion, and conclusions


---
## Week 6 Progress

During Week 6, the project was extended to include incident handling and robustness testing under disrupted traffic conditions.

### Incident Scenario

- Created an incident-style traffic surge scenario using a denser route file
- Built a dedicated SUMO configuration for incident evaluation
- Tested both the fixed-time baseline and the AI-driven controller under the incident

### Evaluation

- Logged simulation outputs for both systems
- Converted XML outputs into CSV for analysis
- Compared:
  - average waiting time
  - average trip duration
  - average time loss
  - vehicles completed

### Key Outcome

This stage adds stress testing to the project and supports evaluation of system robustness, recovery behaviour, and controller performance under dynamic demand conditions.

### Next Steps

- refine recovery-time analysis
- prepare final experiments and plots
- begin final report and presentation preparation


---
## Week 7 Progress

During Week 7, the project was extended with a dashboard to present results, scenario comparisons, and incident analysis in a clear and demo-ready format.

### Dashboard Features

- Built a Streamlit dashboard for visualising project outputs
- Displayed baseline vs AI results across low, medium, and high traffic scenarios
- Added dedicated incident analysis view
- Included summary tables and performance plots
- Added key findings section to support interpretation of results

### Purpose

The dashboard provides a simple interface for demonstrating the integrated AI system and supports final report screenshots, project evaluation, and demo presentation.

### Current Status

The project now includes:
- simulation environment
- baseline controller
- ML prediction model
- adaptive traffic signal controller
- incident handling scenario
- dashboard for presenting results and system behaviour

## Week 8 Progress

During Week 8, the project was extended with advanced evaluation and a reinforcement learning (RL) controller to strengthen the AI component and provide a richer comparison against the baseline and predictive ML controller.

### Reinforcement Learning Extension

- Implemented a Q-learning traffic signal controller as an advanced AI extension
- Defined RL state using live traffic metrics from the SUMO simulation
- Used reward-driven optimisation to learn traffic signal timing policies
- Trained and evaluated the RL controller on the medium traffic scenario
- Compared baseline, original RL, and improved RL performance

### RL Evaluation

- Generated a medium-scenario RL comparison summary
- Compared:
  - fixed-time baseline
  - original RL controller
  - improved RL controller
- Produced a dedicated plot for RL waiting-time comparison

### Incident Reroute Extension

- Added a true road-closure incident scenario with vehicle rerouting
- Tested a stable incident time window for closure and reopening
- Generated comparison outputs for:
  - baseline incident
  - AI incident
  - incident reroute scenario

### Dashboard Updates

- Updated the Streamlit dashboard to include:
  - RL mode description
  - RL analysis section
  - reroute incident comparison in the incident page

### Purpose

This phase strengthens the final project by showing:
- advanced AI experimentation
- comparison of multiple control strategies
- robustness testing under disruption
- clearer evaluation evidence for the final report


## Author

Adnan

