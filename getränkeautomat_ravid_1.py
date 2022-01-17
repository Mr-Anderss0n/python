def Get_Restgeld(v):   #Nimmt Restgeldsumme v und gibt ein Restgeld-dict aus, und reduziert die Kasse um dieses
    v = round(v, 2)
    rest_dict = {}
    for münzwert in kasse:
        rest_dict[münzwert] = 0
        while v >= münzwert and kasse[münzwert] > 0:
            rest_dict[münzwert] += 1
            v -= münzwert
            kasse[münzwert] -= 1
    if v != 0:
        raise ValueError("Nicht genug Kleingeld")
    return  rest_dict

kasse = {2: 4, 1: 0, 0.50: 4, 0.20: 2, 0.10: 3, 0.05: 8}

def Münzeinwurf(n):   #Berechnet die Summe des Einwurfs
    summe = 0
    for münzwert, münzanzahl in n.items():
        summe = summe + münzwert * münzanzahl
        kasse[münzwert] += münzanzahl
    if summe < 2.50:
        return  Get_Restgeld(summe), "Münzen einwerfen"
    return Get_Restgeld(summe - 2.50), "Produkt auswählen"

insert_coin = {2: 1, 1: 0, 0.50: 1}
print(Münzeinwurf(insert_coin))
print(kasse)