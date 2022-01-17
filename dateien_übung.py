target = "primzahlen.py"
lst = []
with open(target, "r+") as datei:
    zeilen = datei.readlines()
    for element in zeilen:
        if "print" in element and element[0] == " ":
            lst.append("    return "+element[10:-2]+"\n")
            #lst.append()
        else:
            lst.append(element)
    datei.seek(0)
    datei.writelines(lst)
datei.close()


