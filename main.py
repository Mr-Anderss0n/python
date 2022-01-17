lst = []
def primzahlen(n):
    for i in range(2, n):
        prim = True
        for j in range(2, i):
            if i % j == 0:
                prim = False
        if prim:
            lst.append(i)
    return lst


def quersumme(n):
    q = 0
    for i in str(n):
        q += int(i)
    return q


def ausführen():
    n = input("Zahl eingeben: ")
    q = input("zweite Zahl:")
    Ergebnis = quersumme(q)
    primz = primzahlen(int(n))
    return primz[Ergebnis]

if __name__ == "__main__":
    a = ausführen()
    print(primzahlen(100)[a])
