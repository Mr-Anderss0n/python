kasse = {2: 4, 1: 0, 0.50: 4, 0.20: 2, 0.10: 3, 0.05: 0}

def Münzeinwurf(n):
    summe = 0
    for münzwert, münzanzahl in n.items():
        summe = summe + münzwert * münzanzahl
        kasse[münzwert] += münzanzahl
    if summe < 2.50:
        print("Münzen einwerfen")
    if summe > 2.50:
        restgeld = summe - 2.50
        print("Artikel wählen", "Restgeld:")
        restmünzen_dict = {}
        for münzwert, münzanzahl in kasse.items():
            restmünzen = restgeld // münzwert
            kasse[münzwert] = münzanzahl - restmünzen
            if kasse[münzwert] < 0:
                restgeld = restgeld % münzwert
                restmünzen_dict[münzwert] = restmünzen
            restgeld = restgeld % münzwert
            restmünzen_dict[münzwert] = restmünzen
        print(restmünzen_dict, restgeld)
    if summe == 2.50:
        print("Artikel wählen")


insert_coin = {2: 1, 1: 1, 0.50: 1, 0.05: 0}
print(Münzeinwurf(insert_coin))
print((kasse))