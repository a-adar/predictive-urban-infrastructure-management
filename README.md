\# AI-Driven Predictive Traffic Signal Management



\## Project Overview



This project focuses on predictive urban infrastructure management using traffic systems as a case study. The system models a small real-world urban road network and applies data-driven techniques to improve traffic flow through predictive and adaptive control.



The core idea is to use simulation data to forecast short-term congestion and dynamically adjust traffic signal behaviour to improve efficiency compared to traditional fixed-time systems.



\---



\## Objectives



\- Build a realistic urban traffic simulation using SUMO

\- Collect time-series traffic data from the simulation

\- Develop a predictive model for short-term congestion

\- Implement an adaptive traffic signal controller

\- Compare performance against a fixed-time baseline system

\- Evaluate performance under different traffic conditions



\---



\## System Architecture



The system consists of the following components:



1\. Traffic Simulation (SUMO)

2\. Data Collection (traffic metrics logging)

3\. Forecasting Model (machine learning)

4\. Adaptive Controller (signal optimisation)

5\. Evaluation Module (performance comparison)



\---



\## Week 1 Progress



During Week 1, the focus was on project planning, system design, and environment setup.



\### Completed Tasks



\- Defined project scope (traffic-based smart infrastructure system)

\- Selected simulation-based approach using SUMO

\- Designed system architecture (simulation → data → prediction → control)

\- Defined baseline system (fixed-time traffic signals)

\- Identified key evaluation metrics:

&#x20; - average waiting time

&#x20; - queue length

&#x20; - travel time

&#x20; - throughput

\- Created project folder structure

\- Set up Python environment and required libraries

\- Installed and configured SUMO

\- Drafted initial project specification



\### Key Decisions



\- Focus on traffic signal optimisation rather than full smart-city system

\- Use a small, controlled road network for experimentation

\- Use simulation-generated data instead of external datasets

\- Start with a fixed-time baseline before introducing AI



\---



\## Week 2 Progress



(You can keep this short for now — your detailed log is in `/docs/weekly\_logs/`)



\- Imported real-world Chicago road network

\- Built working SUMO simulation

\- Generated multiple traffic scenarios

\- Logged simulation outputs

\- Converted XML data to CSV

\- Produced baseline performance metrics and plots



\---

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

\## Author

Adnan

