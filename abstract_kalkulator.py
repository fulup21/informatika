from abc import ABC, abstractmethod

# kontrakt kalkulacky
class AbstractKalkulator(ABC):

    @abstractmethod
    def plus(self, op1: int, op2: int) -> int:
        ...

    @abstractmethod
    def minus(self, op1: int, op2: int) -> int:
        ...

    @abstractmethod
    def multi(self, op1: int, op2: int) -> int:
        ...

    @abstractmethod
    def divide(self, op1: int, op2: int) -> float:
        ...