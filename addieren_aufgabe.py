import re

"""addiert = []
def addierer(zahl):
    zahl = input("Zahl eingeben: ")
    if zahl != "":
        addiert.append((float(zahl)))
        print(sum(addiert))
        addierer(zahl)
    else:
        a = sum(addiert)
        addiert.clear()
        return a


print(addierer(7))"""

"""
def addierer(zahl = 0):
    zahl2 = input("Zahl eingeben: ")
    if not "." in zahl2 and zahl2 != "":
        print("Eingabe muss float sein!")
        return addierer(zahl)
    if zahl2 != "":
        zahl += float(zahl2)
        print(zahl)
        return addierer(zahl)
    else:
        return zahl

print(addierer())"""



patternFloat = r'^[0-9]+.'
patternzwei = r'[0-9]+.[0-9]{2}$'
def addierer():
    Summe = 0
    while True:
        zahl = input("Zahl eingeben: ")
        if zahl == "":
            return Summe
        if re.match(patternFloat, zahl) and re.match(patternzwei, zahl):
            Summe += float(zahl)
            print(round(Summe, 2))
        elif not re.match(patternFloat, zahl):
            print("Eingabe muss zweistelliger float sein!")
            continue
        elif not re.match(patternzwei, zahl):
            print("Eingabe muss zweistellig sein!")
            continue

print(addierer())