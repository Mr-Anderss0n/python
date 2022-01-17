
class Zimmer:
    def __init__(self, zimmernummer, bettenanzahl, balkon = False, meerblick = False, verfügbarkeit = True):
        self.zimmernummer = zimmernummer
        self.bettenanzahl = bettenanzahl
        self.balkon = balkon
        self.meerblick = meerblick
        self.verfügbarkeit = verfügbarkeit


class Hotel:
    def __init__(self, zimmerliste):
        self.zimmerliste = zimmerliste

    def suche(self, bettenanzahl, balkon, meerblick):
        for z in self.zimmerliste:
            if z.bettenanzahl == bettenanzahl and z.balkon == balkon and z.meerblick == meerblick and z.verfügbarkeit == True:
                yield z.zimmernummer

    def gib_z_nach_nummer(self, nummer):
        for z in self.zimmerliste:
            if z.zimmernummer==nummer:
                return z



class Rezeption:
    def __init__(self, hotelobjekt):
        self.hotelobjekt = hotelobjekt
        
    def einchecken(self, wunschzimmernummer):
        zimmer = self.hotelobjekt.gib_z_nach_nummer(int(wunschzimmernummer))
        try:
            print("Check in erfolgt")
            zimmer.verfügbarkeit = False
        except ValueError:
            print("Zimmernummer muss interpretierbare Zahl sein!")
            return

zimmer1 = Zimmer(1, 1, meerblick = True)
zimmer2 = Zimmer(2, 2, balkon = True, meerblick = True)
hotel = Hotel([zimmer1, zimmer2])
R = Rezeption(hotel)
print(*hotel.suche(1, False, True))
print("suche ergab:", [*hotel.suche(2, True, True)][0])

R.einchecken(input("Welche: "))