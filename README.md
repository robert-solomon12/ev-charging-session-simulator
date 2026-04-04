# EV Charging Session Simulator

Python-based EV charging simulation project by **Robert Solomon**.

## Features
- Simulates charging from current SOC to target SOC
- Calculates energy added
- Estimates charging time
- Estimates charging cost
- Logs charging sessions to CSV

## Project Structure
- `main.py` – entry point for the simulator
- `vehicle.py` – EV battery and SOC logic
- `charger.py` – charger configuration
- `session.py` – charging session calculations
- `utils.py` – CSV logging utilities
- `data/` – output session logs

## Example Scenario
- Vehicle: Tesla Model 3
- Battery Capacity: 60 kWh
- Starting SOC: 25%
- Target SOC: 80%
- Charger: 50 kW DC Fast Charger
- Price: €0.35 / kWh

## Future Improvements
- Add charging curve logic
- Add multiple EV profiles
- Add Streamlit dashboard
- Add visual charts for SOC vs time

## Related Work

This project is part of my broader interest in EV systems and charging infrastructure:

- [EV Charging Protocol Implementation (FYP)](https://github.com/robert-solomon12/FYP-Electric-Vehicle-Charging-Protocol-Implementation)  
  A final year project exploring communication between electric vehicles and charging stations, including Vehicle-to-Grid (V2G) concepts and protocol-level interactions.