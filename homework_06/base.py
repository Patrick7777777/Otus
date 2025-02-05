from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: int = 1500, started: bool = False, fuel: int = 50, fuel_consumption: int = 10):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self) -> bool:
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print('Машина завелась')
                return self.started
            else:
                raise LowFuelError(self.fuel)
        else:
            print('Машина уже заведена')
            return self.started

    def move(self, distance: int) -> int:
        if self.started:
            difference = self.fuel - distance * self.fuel_consumption // 100
            if difference < 0:
                raise NotEnoughFuel(abs(difference))
            else:
                return difference
        else:
            print('Заведите машину')


if __name__ == "__main__":
    car = Vehicle(started=False, fuel=50)
    car.start()
    print(car.move(400))
