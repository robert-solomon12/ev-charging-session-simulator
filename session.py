"""
session.py

Contains logic for simulating a charging session.
Author: Robert Solomon
"""

from dataclasses import dataclass
from vehicle import ElectricVehicle
from charger import Charger


@dataclass
class ChargingResult:
    energy_added_kwh: float
    charging_time_hours: float
    charging_cost: float
    final_soc: float


class ChargingSession:
    def __init__(self, vehicle: ElectricVehicle, charger: Charger, target_soc: float):
        self.vehicle = vehicle
        self.charger = charger
        self.target_soc = target_soc

    def run(self) -> ChargingResult:
        energy_needed = self.vehicle.energy_needed_to_target(self.target_soc)

        if self.charger.power_kw <= 0:
            raise ValueError("Charger power must be greater than 0.")

        charging_time = energy_needed / self.charger.power_kw
        charging_cost = energy_needed * self.charger.price_per_kwh
        final_soc = max(self.vehicle.current_soc, self.target_soc)

        return ChargingResult(
            energy_added_kwh=round(energy_needed, 2),
            charging_time_hours=round(charging_time, 2),
            charging_cost=round(charging_cost, 2),
            final_soc=round(final_soc, 2),
        )