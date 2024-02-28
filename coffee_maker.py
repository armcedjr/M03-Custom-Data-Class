"""
Armando Cedano
M03 Custom Data Class 1
This code represents a coffee maker object with the data class along with the UML diagram.
"""

# File: coffee_maker.py

class CoffeeMaker:
    def __init__(self, brand, model, capacity, color, is_single_cup):
        self.__brand = brand
        self.__model = model
        self.__capacity = capacity
        self.__color = color
        self.__is_single_cup = is_single_cup

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_is_single_cup(self):
        return self.__is_single_cup

    def set_is_single_cup(self, is_single_cup):
        self.__is_single_cup = is_single_cup

    def __str__(self):
        return f"{self.__brand} {self.__model} Coffee Maker ({self.__color})"

    def __eq__(self, other):
        if isinstance(other, CoffeeMaker):
            return self.__dict__ == other.__dict__
        return False

"""
--------------------------------------
|            CoffeeMaker             |
--------------------------------------
| - __brand: str                     |
| - __model: str                     |
| - __capacity: int                  |
| - __color: str                     |
| - __is_single_cup: bool            |
--------------------------------------
| + get_brand(): str                 |
| + set_brand(brand: str): None      |
| + get_model(): str                 |
| + set_model(model: str): None      |
| + get_capacity(): int              |
| + set_capacity(capacity: int): None|
| + get_color(): str                 |
| + set_color(color: str): None      |
| + get_is_single_cup(): bool        |
| + set_is_single_cup(is_single_cup: |
|     bool): None                    |
| + __str__(): str                   |
| + __eq__(other: object): bool      |
--------------------------------------
"""
