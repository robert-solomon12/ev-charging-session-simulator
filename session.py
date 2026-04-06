"""
session.py

Contains logic for simulating a charging session.
Author: Robert Solomon
"""

from dataclasses import dataclass, field
from vehicle import ElectricVehicle
from charger import Charger


@dataclass
class ChargingStep:
    time_hours: float
    soc: float
    effective_power_kw: float


@dataclass
class ChargingResult:
    energy_added_kwh: float
    charging_time_hours: float
    charging_cost: float
    final_soc: float
    steps: list[ChargingStep] = field(default_factory=list)


class ChargingSession:
    def __init__(self, vehicle: ElectricVehicle, charger: Charger, target_soc: float):
        self.vehicle = vehicle
        self.charger = charger
        self.target_soc = target_soc

    def _get_power_factor_for_soc(self, soc: float) -> float:
        """
        Return a simplified charging power factor based on SOC.
        """
        if soc < 50:
            return 1.0
        elif soc < 80:
            return 0.7
        else:
            return 0.4

    def _simulate_charging_steps(self) -> tuple[float, list[ChargingStep]]:
        """
        Simulate charging in 1% SOC steps and return:
        - total charging time
        - step-by-step charging data
        """
        total_time_hours = 0.0
        battery_capacity = self.vehicle.battery_capacity_kwh
        current_soc = self.vehicle.current_soc
        steps = []

        # initial point
        steps.append(
            ChargingStep(
                time_hours=0.0,
                soc=current_soc,
                effective_power_kw=self.charger.power_kw * self._get_power_factor_for_soc(current_soc),
            )
        )

        while current_soc < self.target_soc:
            next_soc = min(current_soc + 1, self.target_soc)
            soc_step = next_soc - current_soc

            energy_for_step = (soc_step / 100) * battery_capacity
            power_factor = self._get_power_factor_for_soc(current_soc)
            effective_power = self.charger.power_kw * power_factor

            if effective_power <= 0:
                raise ValueError("Effective charger power must be greater than 0.")

            time_for_step = energy_for_step / effective_power
            total_time_hours += time_for_step
            current_soc = next_soc

            steps.append(
                ChargingStep(
                    time_hours=round(total_time_hours, 4),
                    soc=round(current_soc, 2),
                    effective_power_kw=round(effective_power, 2),
                )
            )

        return total_time_hours, steps

    def run(self) -> ChargingResult:
        """
        Simulate the charging session and return the result.
        """
        energy_needed = self.vehicle.energy_needed_to_target(self.target_soc)

        if self.charger.power_kw <= 0:
            raise ValueError("Charger power must be greater than 0.")

        charging_time, steps = self._simulate_charging_steps()
        charging_cost = energy_needed * self.charger.price_per_kwh
        final_soc = max(self.vehicle.current_soc, self.target_soc)

        return ChargingResult(
            energy_added_kwh=round(energy_needed, 2),
            charging_time_hours=round(charging_time, 2),
            charging_cost=round(charging_cost, 2),
            final_soc=round(final_soc, 2),
            steps=steps,
        )