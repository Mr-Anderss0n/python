import json

class Autor():
    def __init__(self, name):
        self.name = name


class Buch():
    def __init__(self, titel, isbn, autoren):
        self.titel = titel
        self.isbn = isbn
        self.liste_aus_autoren = autoren


class Encoder(json.JSONEncoder):
    def default(self, objekt):
        if isinstance(objekt, Buch):
            return {"titel" : objekt.titel, "isbn" : objekt.isbn, "autoren" : objekt.liste_aus_autoren}
        elif isinstance(objekt, Autor):
            return objekt.name
        else:
            return json.JSONEncoder.default(self, objekt)


rapi = Buch("Bescheurte Namen", "1234", [Autor("Gustav"), Autor("Balthasar"), Autor("Urs")])

with open('json-übung-resultat.json', 'w') as neue_datei:
    json.dump(rapi, neue_datei, cls=Encoder, ensure_ascii=False, indent=4)
