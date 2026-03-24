\# Week 2 Log – Predictive Urban Infrastructure Management



\## Week 2 Goals

\- Build a working traffic simulation using a real-world map

\- Implement a fixed-time baseline traffic control system

\- Generate multiple traffic scenarios (low, medium, high)

\- Log simulation outputs for analysis

\- Convert simulation outputs into usable data

\- Produce initial baseline performance results



\---



\## Work Completed



\### 1. Real-world network creation

\- Downloaded a small section of Chicago from OpenStreetMap

\- Converted OSM data into a SUMO network using `netconvert`

\- Cleaned and simplified the network to ensure usability

\- Verified that roads, junctions, and traffic lights were correctly generated



\---



\### 2. Simulation setup

\- Created SUMO configuration file (`chicago.sumocfg`)

\- Connected:

&#x20; - network file (`chicago.net.xml`)

&#x20; - route files (`.rou.xml`)

\- Successfully ran simulation in SUMO GUI

\- Verified:

&#x20; - vehicles spawn correctly

&#x20; - traffic lights function properly

&#x20; - vehicles obey signals and form queues



\---



\### 3. Traffic scenario generation

\- Generated multiple traffic conditions using `randomTrips.py`:



| Scenario | Description | Period |

|----------|------------|--------|

| Low      | Light traffic | 5 seconds |

| Medium   | Moderate traffic | 2 seconds |

| High     | Heavy traffic | 1 second |



\- Created route files:

&#x20; - `chicago\_low.rou.xml`

&#x20; - `chicago\_medium.rou.xml`

&#x20; - `chicago\_high.rou.xml`



\---



\### 4. Baseline system implementation

\- Established fixed-time traffic signals as the baseline controller

\- No AI or adaptive behaviour implemented at this stage

\- System serves as a reference for future comparison



\---



\### 5. Simulation data logging

\- Configured SUMO to output:

&#x20; - `tripinfo.xml` (vehicle-level metrics)

&#x20; - `edge\_data.xml` (road-level metrics)

\- Ran simulations using `sumo` (non-GUI mode) for faster execution

\- Generated output files for multiple scenarios:

&#x20; - `tripinfo\_medium.xml`

&#x20; - `edge\_data\_medium.xml`

&#x20; - (and equivalents for low/high where applicable)



\---



\### 6. Data processing and conversion

\- Developed Python script to parse XML output

\- Extracted key metrics:

&#x20; - duration

&#x20; - waiting time

&#x20; - time loss

&#x20; - route length

\- Converted XML data into CSV format for analysis:

&#x20; - `tripinfo\_medium.csv`

&#x20; - (later extended to low/high scenarios)



\---



\### 7. Initial analysis and results

\- Computed baseline performance metrics for medium traffic:

&#x20; - total vehicles completed

&#x20; - average travel duration

&#x20; - average waiting time

&#x20; - average time loss



\- Generated first visualisation:

&#x20; - histogram of waiting times

&#x20; - saved to `results/plots/`



\---



\### 8. Scenario comparison

\- Processed low, medium, and high traffic scenarios

\- Created summary table comparing:

&#x20; - average waiting time

&#x20; - travel duration

&#x20; - congestion effects



\- Generated comparison plot:

&#x20; - average waiting time vs traffic level



\---



\## Evidence



\- SUMO simulation screenshots:

&#x20; - full network view

&#x20; - traffic light intersections

&#x20; - vehicle queues

\- Output files:

&#x20; - `results/tripinfo\_medium.xml`

&#x20; - `results/tripinfo\_medium.csv`

&#x20; - `results/scenario\_summary.csv`

\- Plots:

&#x20; - waiting time histogram

&#x20; - scenario comparison chart

\- Code:

&#x20; - XML parsing script

&#x20; - plotting scripts



\---



\## Key Observations



\- The simulation successfully models realistic traffic behaviour using a real-world map

\- Traffic congestion increases significantly with higher vehicle density

\- Average waiting time and time loss rise as traffic demand increases

\- Fixed-time traffic signals do not adapt to changing demand, leading to inefficiencies under heavy load



\---



\## Challenges Encountered



\- PowerShell command syntax issues (line continuation errors)

\- File path and directory structure problems

\- Ensuring SUMO correctly reads network and route files

\- Tuning traffic density to avoid unrealistic gridlock

\- Parsing XML data into usable structured format



\---



\## How Challenges Were Resolved



\- Used single-line commands in PowerShell instead of multi-line syntax

\- Standardised project folder structure (network, routes, configs)

\- Verified file paths and relative references in SUMO config

\- Adjusted traffic generation parameters (`--period`)

\- Built custom Python script to extract and structure XML data



\---



\## Learning Outcomes



\- Learned how to import and simulate real-world road networks using SUMO

\- Understood how traffic density impacts congestion behaviour

\- Gained experience in simulation-based data generation

\- Developed skills in parsing structured XML data for analysis

\- Established a clear baseline system for future AI comparison



\---



\## Next Steps (Week 3)



\- Structure simulation data into a time-series dataset

\- Define prediction target (e.g., queue length or congestion)

\- Build first forecasting model (baseline + ML model)

\- Integrate prediction into system pipeline

\- Begin development of adaptive traffic signal controller



\---



\## Summary



Week 2 successfully established a fully functional traffic simulation system using a real-world map, implemented a fixed-time baseline controller, and generated measurable outputs across multiple traffic scenarios. This provides a strong foundation for developing and evaluating AI-driven predictive control in subsequent weeks.

