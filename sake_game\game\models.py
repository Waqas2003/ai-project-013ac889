from enum import Enum

class SakeType(Enum):
    JUNMAI = 1
    GINJO = 2
    DAIGINJO = 3

class Sake:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price

class Player:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.sakes = []