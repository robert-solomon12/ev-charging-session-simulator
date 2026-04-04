"""
vehicle.py

Defines the ElectricVehicle class used in the charging simulation.
Author: Robert Solomon
"""


class ElectricVehicle:
    def __init__(self, model_name: str, battery_capacity_kwh: float, current_soc: float):
        self.model_name = model_name
        self.battery_capacity_kwh = battery_capacity_kwh
        self.current_soc = current_soc

    def energy_needed_to_target(self, target_soc: float) -> float:
        """
        Calculate how much energy is required to charge
        from the current SOC to the target SOC.
        """
        if target_soc <= self.current_soc:
            return 0.0

        soc_difference = target_soc - self.current_soc
        return (soc_difference / 100) * self.battery_capacity_kwh