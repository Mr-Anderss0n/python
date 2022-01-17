from pathlib import Path

"""def transformer(s):
    for buchstabe in s:
        if buchstabe == buchstabe.lower():
            s = s.upper()
            return s
    return s

with open("dateien_übung_caps_file.txt", "r+", encoding="utf-8") as datei:
    zeilen = datei.readlines()
    datei.seek(0)
    for zeile in zeilen:
        bearbeitet = transformer(zeile)
        datei.write(bearbeitet)

datei.close()

with open("indezierung.md", "rt") as datei:
    zeilen = datei.readlines()
datei.close()

with open("dateien_übung_caps_file.txt", "wt") as datei2:
    datei2.writelines(zeilen)
datei2.close()"""


def korrigiert(z):
    pattern = "Rauchen"
    if pattern in z:
        pos = z.find(pattern)
        return z[0:pos] + "Sport " + z[pos + 8:]
    return z

with open("dateien_übung_caps_file.txt", "r+") as datei3:
    zeilen = datei3.readlines()
    lst = [] # zeilen = [korrigiert(l) for l in zeilen]
    for zeile in zeilen:
        new = korrigiert(zeile)
        lst.append(new)
datei3.close()

with open("dateien_übung_caps_file.txt", "wt") as datei4:
    datei4.writelines(lst)
datei4.close()

print(Path.cwd())
print(Path.cwd().parent)
print([str(p.relative_to(Path.cwd())) for p in Path.cwd().glob("*.txt")])