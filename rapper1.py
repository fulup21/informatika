from kalkulator import Kalkulator
from abstract_kalkulator import AbstractKalkulator


class Wrapper1Kalkulator(Kalkulator):

    def __init__(self, delegate: AbstractKalkulator):
        self._delegate = delegate

    def plus(self, op1: int, op2: int) -> int:
        print("plus")
        return self._delegate.plus(op1, op2)

    def minus(self, op1: int, op2: int) -> int:
        print("minus")
        return self._delegate.minus(op1, op2)

    def multi(self, op1: int, op2: int) -> int:
        print("multi")
        return self._delegate.multi(op1, op2)

    def divide(self, op1: int, op2: int) -> float:
        print("divide")
        return self._delegate.divide(op1, op2)