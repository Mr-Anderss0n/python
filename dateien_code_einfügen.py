target = "kleinstes_vielfaches.py"
with open("primzahlen.py", "r+") as datei:
    zeilen = datei.readlines()
    lst = []
    actual_code = False
    for zeile in zeilen:
        if zeile[0:len( "def primzahlen2(m):")] == "def primzahlen2(m):":
            actual_code = True
        elif actual_code and (zeile[0] != " " and zeile[0] != "\n"):
            actual_code = False
        if actual_code:
            lst.append(zeile)

datei.close()
with open(target, "a") as datei:
    datei.writelines(lst)
datei.close()
"""
target = "kleinstes_vielfaches.py"
with open("primzahlen.py", "r+") as datei:
    zeilen = datei.readlines()
    primzahl_kopie = []
    currently_reading = False
    for zeile in zeilen:
        if zeile[0:len( "def primzahlen2(m):")] == "def primzahlen2(m):":
            currently_reading = True
        elif currently_reading and (zeile[0] != " " and zeile[0] != "\n"):
            currently_reading = False
        if currently_reading:
            primzahl_kopie.append(zeile)
datei.close()


with open(target, "r") as datei:
    zeilen = datei.readlines()
    edited_code = []
    currently_NOT_reading = False
    for zeile in zeilen:
        if zeile[0:len("def vielfaches(n, k):")] == "def vielfaches(n, k):":
            currently_NOT_reading = True
        elif currently_NOT_reading and (zeile[0] != " " and zeile[0] != "\n"):
            for line in primzahl_kopie:
                edited_code.append(line)
            currently_NOT_reading = False
        if not currently_NOT_reading:
            edited_code.append(zeile)
datei.close()
print(edited_code)
print(primzahl_kopie)
with open(target, "w") as datei:
    datei.writelines(edited_code)
datei.close()"""
