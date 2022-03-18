spieleraccounts = {}
chronologie = []

def account_und_punkteverwaltung():  #Erzeugt Spieleraccounts und verarbeitet die Vergabe von Punkten
    #Wenn erster durchlauf werden Spieler angelegt
    if len(list(spieleraccounts)) == 0:
        spielernummer = 1
        while True:
            print("                                                                                        ")
            name = input(f"Name Spieler {spielernummer} eingeben oder Eingabe mit Enter beenden: ")
            if name == "":
                break
            punkte = int(input(f"Punkte {name} eingeben: "))
            spieleraccounts[name] = punkte
            satz = [name, punkte]
            chronologie.append(satz)
            spielernummer += 1

    #Wenn Spieler bereits existieren wird nur nach Punkten gefragt
    else:
        for spieler in spieleraccounts.keys():
            print("                                                                                        ")
            punkte = int(input(f"Punkte {spieler} eingeben: "))
            spieleraccounts[spieler] += punkte
            satz = [spieler, punkte]
            chronologie.append(satz)
    ausgabe_spieleraccounts()

    return spieleraccounts


def spielabschluss():  #Ermittelt den Sieger und zeigt die Zahlungsformalitäten an
    #Ermittelt die höchste Punktzahl und den Sieger
    höchste = 0
    name = ""
    for spieler, punkte in spieleraccounts.items():
        if punkte > höchste:
            höchste = punkte
            name = spieler

    #Prüft ob es mehrere Sieger gibt
    sieger = [name]
    for spieler, punkte in spieleraccounts.items():
        if punkte == höchste and spieler != name:
            sieger.append(spieler)

    #Berechnet und zeigt an wer wie viel an wen zahlen muss
    if len(sieger) == 1:
        print("                                                                                 ")
        print(f"{sieger[0]} hat gewonnen!!!")

        for spieler, punkte in spieleraccounts.items():
            if punkte < höchste:
                differenz = (höchste - punkte) // 2 * 0.10
                print("{:s} muss {:.2f} Euro an {:s} zahlen" .format(spieler, differenz, name))
    else:
        print("                                                                                        ")
        print(f"{name} und {sieger[1]} haben einen Gleichstand mit je {höchste} Punkten")
        for spieler, punkte in spieleraccounts.items():
            if punkte < höchste:
                differenz = (höchste - punkte) // 2 * 0.10 // len(sieger)
                print(f"{spieler} muss je {differenz} Euro an {name} und {sieger[1]} zahlen")
    ausgabe_spieleraccounts()
    abfrage_nach_reset()

    return spieleraccounts
        

def spieler_hinzufügen():  #Neuen Spieler anlegen
    print("                                                                                        ")
    name = input("Name neuer Spieler eingeben: ")
    punkte = int(input(f"Punkte {name} eingeben: "))
    spieleraccounts[name] = punkte
    print("                                                                                        ")
    print(f"{name} wurde hinzugefügt")
    ausgabe_spieleraccounts()

    return spieleraccounts


def spieler_entfernen():  #Entfernt Spieler aus Spieleraccount
    print("                                                                                        ")
    name = input("Welcher Spieler soll entfernt werden: ")
    spieleraccounts.pop(name)
    print("                                                                                        ")
    print(f"{name} wurde entfernt")
    ausgabe_spieleraccounts()

    return spieleraccounts


def ausgabe_spieleraccounts():  #Zeigt den aktuellen Spielstand an
    print("                                                                                        ")
    print("Aktueller Spielstand: ")
    print("                                                                                        ")
    for spieler, punkte in spieleraccounts.items():
        print("{0:<10s} {1:>8d} Punkte" .format(spieler, punkte))
    print("________________________________________________________________________________________")


def chronologie_anzeigen():  #Zeigt den chronologischen Ablauf an
    print("                                                                                        ")
    print("Chronologie:")
    print("                                                                                        ")
    for element in chronologie:
        print(element)
    print("________________________________________________________________________________________")


def abfrage_nach_reset():  #Abfrage ob die Spieleraccounts resetet werden sollen
    print("                                                                                        ")
    abfrage = input("Sollen die Spieleraccounts resetet werden?\n\n1 ja\n2 nein\nAuswahl: ")
    if abfrage == "1":
        print("                                                                                        ")
        print("Spieleraccounts resetet")
        spieleraccounts_reseten()
    elif abfrage == "2":
        print("                                                                                        ")
        print("Spieleraccounts bleiben erhalten")
        ausgabe_spieleraccounts()
        print("________________________________________________________________________________________")
    else:
        print("Falsche Eingabe")
        abfrage_nach_reset()


def spieleraccounts_reseten():  #Setzt alle Spieleraccounts auf null, Spieleraccounts bleiben bestehen
    for spieler in spieleraccounts.keys():
        spieleraccounts[spieler] = 0
    ausgabe_spieleraccounts()

    return spieleraccounts


def ausführen():  #Interface
    while True:
        print("                                                                                        ")
        frage = "Was möchtest du tun?\n\n1 Punkte eingeben\n2 Abschluss anzeigen\n3 Neuen Spieler hinzufügen\n4 Spieler entfernen\n5 aktuellen Spielstand anzeigen\n6 Chronologie anzeigen\n7 Spieleraccounts reseten\n8 Programm beenden\nAuswahl: "
        abfrage = input(f"{frage}")
        print("________________________________________________________________________________________")
        if abfrage == "1":
            account_und_punkteverwaltung()
        elif abfrage == "2":
            spielabschluss()
        elif abfrage == "3":
            spieler_hinzufügen()
        elif abfrage == "4":
            spieler_entfernen()
        elif abfrage == "5":
            ausgabe_spieleraccounts()
        elif abfrage == "6":
            chronologie_anzeigen()
        elif abfrage == "7":
            spieleraccounts_reseten()
        elif abfrage == "8":
            break
        else:
            print("Falsche Eingabe")
            print("Eingabe wiederholen")
    return spieleraccounts


ausführen()