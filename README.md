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



(You can keep this short for now — your detailed log is in `/docs/weekly\_logs/`)



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


## Author

Adnan

