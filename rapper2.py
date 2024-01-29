from kalkulator import Kalkulator
from abstract_kalkulator import AbstractKalkulator


class Wrapper2Kalkulator(Kalkulator):

    def __init__(self, delegate: AbstractKalkulator):
        self._delegate = delegate
        self.pamet = []

    def plus(self, op1: int, op2: int) -> int:
        self.pamet.append("plus" + " " + str(op1) + " " + str(op2) + " " + str(self._delegate.plus(op1, op2)))
        return self._delegate.plus(op1, op2)

    def minus(self, op1: int, op2: int) -> int:
        self.pamet.append("minus" + " " + str(op1) + " " + str(op2) + " " + str(self._delegate.minus(op1, op2)))
        return self._delegate.minus(op1, op2)

    def multi(self, op1: int, op2: int) -> int:
        self.pamet.append("multi" + " " + str(op1) + " " + str(op2) + " " + str(self._delegate.multi(op1, op2)))
        return self._delegate.multi(op1, op2)

    def divide(self, op1: int, op2: int) -> float:
        self.pamet.append("divide" + " " + str(op1) + " " + str(op2) + " " + str(self._delegate.divide(op1, op2)))
        return self._delegate.divide(op1, op2)

    def memory(self) -> list:
        return self.pamet
