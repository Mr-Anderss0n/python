def sample2(n):
    print(n)

def main(k):
    sample2(k)


def vielfaches(n, k):
    try:
        akk = 0
        for i in range(k):
            akk += n
            if akk % k == 0:
                return akk
        return akk
    except TypeError:
        print("fehleingabe für parameter 2, default value 5 benutzen...")
        return vielfaches(n, 5)


def testvielfaches():
    print(vielfaches(4, "i"))


if __name__ == "__main__":
    testvielfaches()def primzahlen2(m):
    primzahlen = []
    for i in range(2, m):
        primzahl = True
        for j in range(2, i):
            if i % j == 0:
                primzahl = False
        if primzahl:
            primzahlen.append(i)

    return primzahlen

def primzahlen2(m):
    primzahlen = []
    for i in range(2, m):
        primzahl = True
        for j in range(2, i):
            if i % j == 0:
                primzahl = False
        if primzahl:
            primzahlen.append(i)

    return primzahlen

def primzahlen2(m):
    primzahlen = []
    for i in range(2, m):
        primzahl = True
        for j in range(2, i):
            if i % j == 0:
                primzahl = False
        if primzahl:
            primzahlen.append(i)

    return primzahlen

def primzahlen2(m):
    primzahlen = []
    for i in range(2, m):
        primzahl = True
        for j in range(2, i):
            if i % j == 0:
                primzahl = False
        if primzahl:
            primzahlen.append(i)

    return primzahlen

def primzahlen2(m):
    primzahlen = []
    for i in range(2, m):
        primzahl = True
        for j in range(2, i):
            if i % j == 0:
                primzahl = False
        if primzahl:
            primzahlen.append(i)

    return primzahlen

def primzahlen2(m):
    primzahlen = []
    for i in range(2, m):
        primzahl = True
        for j in range(2, i):
            if i % j == 0:
                primzahl = False
        if primzahl:
            primzahlen.append(i)

    return primzahlen

def primzahlen2(m):
    primzahlen = []
    for i in range(2, m):
        primzahl = True
        for j in range(2, i):
            if i % j == 0:
                primzahl = False
        if primzahl:
            primzahlen.append(i)

    return primzahlen

