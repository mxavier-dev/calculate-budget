from abc import ABC, abstractmethod

class RealState(ABC):
    @abstractmethod
    def calculate_budget(self) -> float:
        pass


class Apartment(RealState):
    def __init__(self, rooms=1, garage=False, kids=False):
        self.budget:float = 700.00
        self.rooms:int = rooms
        self.garage:bool = garage
        self.kids:bool = kids

    def calculate_budget(self) -> float:
        if self.rooms == 2:
            self.budget += 200
        if self.garage:
            self.budget += 300
        if not self.kids:
            self.budget *= 0.95
        return self.budget


class House(RealState):
    def __init__(self, rooms=1, garage=False):
        self.budget:float = 900.00
        self.rooms:int = rooms
        self.garage:bool = garage

    def calculate_budget(self) -> float:
        if self.rooms == 2:
            self.budget += 250
        if self.garage:
            self.budget += 300
        return self.budget


class Studio(RealState):
    def __init__(self, garage_spaces=0):
        self.budget:float = 1200.00
        self.garage_spaces:int = garage_spaces

    def calculate_budget(self) -> float:
        if self.garage_spaces > 0:
            self.budget += 250
            if self.garage_spaces > 2:
                self.budget += (60 * self.garage_spaces - 2)
        return self.budget