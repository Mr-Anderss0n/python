import time

class Rechner:
    def __init__(self, genauigkeit):
        self.genauigkeit = genauigkeit

    def primzahlen(self, n):
        lst = []
        for i in range(2, n):
            prim = True
            for j in range(2, i):
                if i%j == 0:
                    prim = False
            if prim:
                lst.append(i)
        return lst

    def rest(self, divisor, divident):
        for i in range(divisor):
            if i * divident > divisor:
                break

        rest = divisor - (i-1) * divident
        return rest

prim = Rechner(3)
start = time.time()
for i in range(1000):
    prim.primzahlen(20)
print(time.time() - start)
prim.rest(12, 7)



