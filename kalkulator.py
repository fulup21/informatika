from abstract_kalkulator import AbstractKalkulator


class Kalkulator(AbstractKalkulator):
    """
    Ten jediny kdo opravdu pocita.
    """

    def plus(self, op1: int, op2: int) -> int:
        return op1 + op2

    def minus(self, op1: int, op2: int) -> int:
        return op1 - op2

    def multi(self, op1: int, op2: int) -> int:
        return op1 * op2

    def divide(self, op1: int, op2: int) -> float:
        return op1 / op2