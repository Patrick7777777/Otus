"""
создайте класс `Car`, наследник `Vehicle`
"""


from base import Vehicle
from engine import Engine


class Car(Vehicle):
    def __init__(self, weight: int, started: bool, fuel: int, fuel_consumption: int):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine


if __name__ == "__main__":
    my_engine = Engine(volume=2.0, pistons=4)
    my_car = Car(1500, True, 50, 10)
    my_car.set_engine(my_engine)
    print(f"Машина: вес {my_car.weight}, бензин {my_car.fuel} литров, "
          f"двигатель: {my_car.engine.volume} с {my_car.engine.pistons} поршнями")

