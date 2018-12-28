from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass


class Pclass(ABC):

    def __init__(self, name, baseMoveSpeed, baseHealth):
        self.name = name
        self.baseMoveSpeed = baseMoveSpeed
        self.baseHealth = baseHealth
        super().__init__()

    @abstractmethod
    def toString(self):
        return self.name



class Fighter(Pclass):

    def __init__(self):
        self.baseRage = 100
        super().__init__("Fighter", 10, 100)

    def toString(self):
        return self.name

class Wiken(Pclass):

    def __init__(self):
        self.baseMana = 100
        super().__init__("Wiken", 6, 80)
    def toString(self):
        return self.name
