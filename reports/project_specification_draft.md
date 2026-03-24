\# Project Specification



\## 1. Background



Urban traffic congestion is a major challenge in modern cities, leading to increased travel times, fuel consumption, and environmental impact. Traditional traffic signal systems typically rely on fixed timing schedules that do not adapt to real-time changes in traffic demand. As a result, these systems often perform poorly under dynamic conditions such as rush hours, unexpected surges, or road disruptions.



Recent advances in artificial intelligence and data-driven systems provide an opportunity to improve traffic management through predictive modelling and adaptive control. By forecasting traffic conditions and adjusting signal timings accordingly, AI-based systems can optimise traffic flow, reduce congestion, and improve overall system efficiency.



This project explores the design and implementation of a predictive traffic management system within a simulated urban environment.



\## 2. Aim



The aim of this project is to develop an AI-driven traffic management system that predicts short-term congestion and dynamically adjusts traffic signal timings to improve efficiency and system stability.



\## 3. Objectives



\- Build a simulated urban traffic network with multiple intersections

\- Collect time-series traffic data from the simulation

\- Develop a forecasting model to predict short-term congestion

\- Implement an adaptive traffic signal controller based on predictions

\- Compare performance against a fixed-time baseline system

\- Evaluate system performance under normal and disrupted conditions

\- Visualise system behaviour using a simple dashboard



\## 4. Proposed Solution



The proposed system consists of five main components. First, a traffic simulation environment will be created using a small urban road network with multiple intersections and traffic signals. The simulation will generate traffic flow data under different scenarios, including normal conditions, peak demand, and disruptions.



Second, traffic data such as queue length, vehicle count, and waiting time will be collected at regular intervals and stored for analysis.



Third, a machine learning model will be developed to perform time-series forecasting and predict short-term congestion levels at each intersection.



Fourth, an adaptive traffic signal controller will use these predictions to dynamically adjust signal timings in real time.



Finally, a dashboard will be implemented to visualise traffic conditions, predictions, and system performance, allowing comparison between the AI-controlled system and a fixed-time baseline.



\## 5. Actors and Use Cases



\- Traffic Operator: Monitors system performance and results

\- AI Controller: Makes decisions on traffic signal timings

\- Simulation System: Generates traffic data and environment

\- Vehicles: Represent traffic flow within the system



\- Start simulation

\- Generate traffic scenarios (normal, peak, disruption)

\- Collect traffic data from simulation

\- Predict future congestion using AI model

\- Adjust traffic signal timings dynamically

\- Monitor traffic performance through dashboard

\- Compare AI system with baseline system



\## 6. Functional Requirements



\- The system shall simulate traffic flow across multiple intersections

\- The system shall record traffic metrics such as queue length and waiting time

\- The system shall predict short-term congestion using historical data

\- The system shall dynamically adjust traffic signal timings

\- The system shall support different traffic scenarios including disruptions

\- The system shall provide visual output of system performance

\- The system shall allow comparison between baseline and AI-controlled modes



\## 7. Non-Functional Requirements



\- The system should be modular and easy to extend

\- The system should produce reproducible results across experiments

\- The system should respond within a reasonable simulation time interval

\- The dashboard should be clear and easy to interpret

\- The AI component should be clearly separable for evaluation

\- The system should remain stable under high traffic load scenarios



\## 8. Timeline / Roadmap



Week 1: Project planning, specification, and environment setup  

Week 2: Build initial traffic simulation  

Week 3: Implement baseline traffic signal controller and data logging  

Week 4: Develop and test forecasting model  

Week 5: Implement adaptive traffic control system  

Week 6: Add disruption scenarios and improve controller  

Week 7: Build dashboard and visualisations  

Week 8: Run experiments and collect results  

Week 9: Analyse results and refine system  

Week 10+: Finalise report and prepare presentation

