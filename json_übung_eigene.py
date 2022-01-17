import json

class Gericht():
    def __init__(self, gericht, zutaten):
        self.gericht = gericht
        self.zutaten = zutaten

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Gericht):
            return {"Gericht": obj.gericht, "Zutaten": obj.zutaten}
        else:
            return json.JSONEncoder.default(self, obj)

class Decoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.hook, *args, **kwargs)

    def hook(self, js_objekt):
        if "Gericht" not in js_objekt:
            return js_objekt
        else:
            return Gericht(js_objekt["Gericht"], js_objekt["Zutaten"])

ger1 = Gericht("Gulasch", ["Fleisch", "Zwiebel", "Paprika"])
var = json.dumps(ger1, cls = Encoder, ensure_ascii= False, indent=4)
copy = json.loads(var, cls= Decoder)
print(var)
print(copy)