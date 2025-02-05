"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight: int, started: bool, fuel: int, fuel_consumption: int, cargo: float, max_cargo: float):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, luggage: float):
        current_cargo = luggage + self.cargo
        if current_cargo > self.max_cargo:
            raise CargoOverload(current_cargo - self.max_cargo)
        else:
            self.cargo = current_cargo

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo


if __name__ == '__main__':
    plane = Plane(3000, False, 1000, 100, 1000, max_cargo=1500)
    plane.load_cargo(200)
    print(plane.cargo)
    prev_cargo = plane.remove_all_cargo()
    print(plane.cargo, prev_cargo)


