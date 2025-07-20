# Vaccination Strategy Comparison in COVID-19 Infection Using Excitable Media on Random Graphs

This project investigates the dynamics of COVID-19 infection spread and evaluates the effectiveness of different vaccination strategies—mass vs. targeted—using excitable media on Barabási–Albert random graphs. The approach leverages artificial life techniques to simulate individual-based interactions and model state transitions (susceptible, infected, recovered, dead, vaccinated) based on probabilistic rules.

## Author

**Eshani Nandy**  
Department of Electrical and Computer Engineering  
University of Waterloo  
[enandy@uwaterloo.ca](mailto:enandy@uwaterloo.ca)

---

## Overview

- **Goal 1**: Validate that excitable media on random graphs can simulate infection dynamics similar to the SIR model.
- **Goal 2**: Compare the effectiveness of mass and targeted vaccination strategies in achieving herd immunity.

This simulation uses a population of 1,000 nodes on a scale-free Barabási–Albert graph with state transitions governed by realistic COVID-19 parameters. Both vaccination strategies are simulated over 100 time steps.

---

## Simulation Model

- **Graph Type**: Barabási–Albert (scale-free network)
- **Population**: 1,000 nodes
- **States**: Susceptible, Infected, Recovered, Dead, Vaccinated
- **R₀ (Delta variant)**: 5.08
- **Time Steps**: 100
- **Vaccination Rate**: 5% of eligible nodes per time step

### State Transitions (Excitable Media):
- Susceptible → Infected
- Infected → Recovered / Dead
- Susceptible / Recovered → Vaccinated

---

## Vaccination Strategies

### 1. Mass Vaccination
- Randomly selects 5% of all eligible nodes (susceptible or recovered) at each time step
- Achieves herd immunity in simulation
- Results in higher vaccination and lower death rate

### 2. Targeted Vaccination
- Vaccinates nodes with high connectivity or proximity to infected nodes
- Also limited to 5% of eligible nodes per time step
- Relies heavily on natural recovery and fails to achieve herd immunity in current setup

---

## Results Summary

- **Infection Spread** matches the trend of traditional SIR models.
- **Mass Vaccination**:
  - Achieves herd immunity (~80% immunity)
  - Fewer deaths
  - Higher vaccine-driven immunity

- **Targeted Vaccination**:
  - Fails to reach herd immunity
  - Most immunity from natural recovery
  - Higher overall infection and death rate compared to mass vaccination

---

## Metrics Tracked

- Infection Rate
- Recovery Rate
- Death Rate
- Vaccination Rate
- Immunity % (Vaccinated + Recovered)
- Susceptibility over time
- Herd Immunity Threshold: 1 - (1 / R₀) ≈ 0.803

---

## Running the Simulation

### Prerequisites
- Python 3.x
- NetworkX
- Matplotlib
- NumPy

### Clone and Run

```bash
git clone https://github.com/eshaninandy/VaccinationStrategyComparison
cd VaccinationStrategyComparison
python simulate.py
```
