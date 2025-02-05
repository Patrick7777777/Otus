"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, fuel_level: int):
        self.fuel_level = fuel_level
        self.message = f'Бензин кончился, осталось {self.fuel_level} литров'
        super().__init__(self.message)


class NotEnoughFuel(Exception):
    def __init__(self, fuel: int):
        self.fuel = fuel
        self.message = f'Для поездки недостаточно {fuel} литров бензина'
        super().__init__(self.message)


class CargoOverload(Exception):
    def __init__(self, overload: float):
        self.message = f'Перегрузка на {overload} кг'
        super().__init__(self.message)

