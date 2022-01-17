def bindec(n):  # string eingeben
    k = 1
    erg = 0
    for i in n:
        power = len(n) - k
        k += 1
        erg += 2**power * int(i)
    return erg


def decbin(m):  # integer eingeben
    b = ""
    while m != 0:
        rest = m % 2
        b = str(rest) + b
        m /= 2
        m = int(m)
    return b


def main():
    broj = int(input("dezimalzahl eingeben: "))
    print(str(broj) + " als binärzahl ist " + decbin(broj))

    zahl = input("binärzahl eingeben: ")
    print(str(zahl) + " als dezimalzahl ist " + str(bindec(zahl)))


if __name__ == "__main__":  # führt aus, wenn das programm direkt aufgerufen wird
    main()





