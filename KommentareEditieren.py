target = "datei_programmieren.txt"
with open(target, "r+") as datei:
    zeilen = datei.readlines()
    lst = []
    for zeile in zeilen:
        akku = ""
        for element in zeile:
            if element != "#":
                akku += element
            else:
                akku += "\n"
                break
        lst.append(akku)
    print(lst)

with open(target, "w") as datei:
    datei.writelines(lst)
datei.close()


