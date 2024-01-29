from kalkulator import Kalkulator
from abstract_kalkulator import AbstractKalkulator
# from rapper1 import Wrapper1Kalkulator
# from rapper2 import Wrapper2Kalkulator
from rapper3 import Wrapper3Kalkulator



# test pouziti:
# kalkulator : AbstractKalkulator = Wrapper1Kalkulator(Kalkulator())
# kalkulator : AbstractKalkulator = Wrapper2Kalkulator(Kalkulator())
kalkulator : AbstractKalkulator = Wrapper3Kalkulator(Kalkulator())


# zde zavolejte více než jen jednu operaci, abyste ověřili funkčnost
r = kalkulator.plus(2,3)
r = kalkulator.multi(2,3)
r = kalkulator.minus(4,7)
r = kalkulator.minus(4,7)
print(kalkulator.keška())
# x = kalkulator.minus(2,3)
print(f"2 plus 3 je {r}")
print("Na Wrapperu pracovali Šimon Klíma (7.B) a Filip Dzupin (7.A)")
# print(kalkulator.memory())
