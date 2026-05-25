from abc import ABC, abstractmethod

class RealState(ABC):
    @abstractmethod
    def calculate_budget(self) -> float:
        pass


class Apartment(RealState):
    budget:float = 700.00

    def __init__(self, rooms=1, garage=False, kids=False):
        self.rooms:int = rooms
        self.garage:bool = garage
        self.kids:bool = kids

    def calculate_budget(self) -> float:
        if self.rooms == 2:
            Apartment.budget += 200
        if self.garage:
            Apartment.budget += 300
        if not self.kids:
            Apartment.budget *= 0.95
        return Apartment.budget


class House(RealState):
    budget:float = 900.00

    def __init__(self, rooms=1, garage=False):
        self.rooms:int = rooms
        self.garage:bool = garage

    def calculate_budget(self) -> float:
        if self.rooms == 2:
            House.budget += 250
        if self.garage:
            House.budget += 300
        return House.budget


class Studio(RealState):
    budget:float = 1200.00

    def __init__(self, garage_spaces=0):
        self.garage_spaces:int = garage_spaces

    def calculate_budget(self) -> float:
        if self.garage_spaces > 0:
            Studio.budget += 250
            if self.garage_spaces > 2:
                Studio.budget += (60 * self.garage_spaces - 2)
        return Studio.budget