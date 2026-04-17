\# Hierarchical RL Summary



A hierarchical reinforcement learning extension was added to the project.



\## Architecture

\- Global RL agent:

&#x20; - observes network-level traffic state

&#x20; - selects global control mode

\- Local RL agent:

&#x20; - observes junction-level state

&#x20; - adjusts signal timing locally

&#x20; - uses global mode as part of its state



\## Motivation

This design was introduced to move beyond a single global RL controller and better reflect the structure of real-world urban traffic management systems.



\## Outcome

The hierarchical RL controller was successfully implemented and evaluated on the medium scenario. It is presented as an advanced AI extension that strengthens the technical depth of the project, regardless of whether it ultimately outperforms the fixed-time baseline.



\## Not Enough Time

Although running successfully. Because I was working alone I did not have time to improve the times.

