with open("datei_programmieren.txt", "r") as datei:

    text = datei.read()
    
    while True:
        zeile = datei.readline()
        print(zeile)
        if zeile == "":
            break

    zeilenliste = datei.readlines()
    print(zeilenliste)
    print(zeilenliste[0] + "\n" + zeilenliste[2])

datei.close()