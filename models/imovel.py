from abc import ABC, abstractmethod

class Imovel(ABC):
    @abstractmethod
    def calcular_aluguel(self) -> float:
        pass


class Apartamento(Imovel):
    def __init__(self, qtnd_quartos=1, garagem=False, crianca=False):
        self.orcamento:float = 700.00
        self.quarto:int = qtnd_quartos
        self.garagem:bool = garagem
        self.crianca:bool = crianca

    def calcular_aluguel(self) -> float:
        if self.quarto == 2:
            self.orcamento += 200
        if self.garagem:
            self.orcamento += 300
        if not self.crianca:
            self.orcamento *= 0.95
        return self.orcamento


class Casa(Imovel):
    def __init__(self, qtnd_quartos=1, garagem=False):
        self.orcamento:float = 900.00
        self.quartos:int = qtnd_quartos
        self.garagem:bool = garagem

    def calcular_aluguel(self) -> float:
        if self.quartos == 2:
            self.orcamento += 250
        if self.garagem:
            self.orcamento += 300
        return self.orcamento


class Estudio(Imovel):
    def __init__(self, vagas_garagem=0):
        self.orcamento:float = 1200.00
        self.vagas_garagem:int = vagas_garagem

    def calcular_aluguel(self) -> float:
        if self.vagas_garagem:
            self.orcamento += 250
            if self.vagas_garagem > 2:
                self.orcamento += (60 * self.vagas_garagem-2)
        return self.orcamento