from kalkulator import Kalkulator
from abstract_kalkulator import AbstractKalkulator


class Wrapper3Kalkulator(Kalkulator):

    def __init__(self, delegate: AbstractKalkulator):
        self._delegate = delegate
        self.cache = {}

    def plus(self, op1: int, op2: int) -> int:
        if self.cache.get(("plus" + " " + str(op1) + " " + str(op2))):
            print("vytisknuto z kešky")
            return self.cache.get(("plus" + " " + str(op1) + " " + str(op2)))
        else:
            self.cache.update({("plus" + " " + str(op1) + " " + str(op2)): str(self._delegate.plus(op1, op2))})
            print("přidáno do kešky")
            return self._delegate.plus(op1, op2)

    def minus(self, op1: int, op2: int) -> int:
        if self.cache.get(("minus" + " " + str(op1) + " " + str(op2))):
            print("vytisknuto z kešky")
            return self.cache.get(("minus" + " " + str(op1) + " " + str(op2)))
        else:
            self.cache.update({("minus" + " " + str(op1) + " " + str(op2)): str(self._delegate.minus(op1, op2))})
            print("přidáno do kešky")
            return self._delegate.minus(op1, op2)

    def multi(self, op1: int, op2: int) -> int:
        if self.cache.get(("multi" + " " + str(op1) + " " + str(op2))):
            print("vytisknuto z kešky")
            return self.cache.get(("multi" + " " + str(op1) + " " + str(op2)))
        else:
            self.cache.update({("multi" + " " + str(op1) + " " + str(op2)): str(self._delegate.multi(op1, op2))})
            print("přidáno do kešky")
            return self._delegate.multi(op1, op2)

    def divide(self, op1: int, op2: int) -> float:
        if self.cache.get(("multi" + " " + str(op1) + " " + str(op2))):
            print("vytisknuto z kešky")
            return self.cache.get(("multi" + " " + str(op1) + " " + str(op2)))
        else:
            self.cache.update({("multi" + " " + str(op1) + " " + str(op2)): str(self._delegate.multi(op1, op2))})
            print("přidáno do kešky")
            return self._delegate.multi(op1, op2)

    def keška(self) -> dict:
        return (self.cache)
