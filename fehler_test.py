"""def primzahlen(n):
    try:
        lst = []
        for i in range(2, n):
            prim = True
            for j in range(2, i):
                if i % j == 0:
                    prim = False
            if prim:
                lst.append(i)
        return lst
    except TypeError:
        print("Kein integer!!!")
        neue_zahl = input("Geben Sie einen integer ein:")
        return primzahlen(int(neue_zahl))

print(primzahlen(34))"""


def list_amplifier(l):
    try:
        l = [1/i for i in l]
        return l
    except Exception as e:
        if type(e) == ZeroDivisionError:
            print("Teilen durch Null nicht möglich. Funktion wird ohne Nullen wieder ausgeführt.")
            neues_array = [i for i in l if i != 0]
            l = [1 / i for i in neues_array]
            return l
        if type(e) == TypeError:
            raise ValueError("Funktion nimmt nur zahlwertige Listen!!!")
        else:
            print("unbekannter Fehler. Abbruch")
            raise e
            # mit raise bricht ab, man kann vorher print statement machen

print(list_amplifier([0,1,2,3,4]))
print(list_amplifier(7))


"""try:
    raise TypeError("Fehler")
except TypeError:
    print("excepting my own error")"""



