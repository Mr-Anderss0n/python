with open("binärzahlen.py", "r+") as datei:
    zeilen = datei.readlines()
    lst = []
    code = False
    for zeile in zeilen:
        if zeile[0:len("def bindec(m):")] == "def bindec(m):":
            code = True
        elif code and (zeile[0] != " " and zeile[0] != "\n"):
            code = False
        if code:
            lst.append(zeile)
    print(lst)
datei.close()
