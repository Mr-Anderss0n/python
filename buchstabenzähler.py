text = "das ist ein text um zu testen wie oft jeder buchstabe in ihm vorkommt"

def zaehler(t): # nimmt einen text und zeigt an wie oft jeder buchstabe vorkommt
    t = t.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    zaehlung = {}
    for buchstabe in t:
        if buchstabe not in zaehlung and buchstabe in alphabet:
            zaehlung[buchstabe] = 1
        elif buchstabe in zaehlung:
            zaehlung[buchstabe] = zaehlung[buchstabe] +1
    return zaehlung


def prozent(d): # nimmt ein dictionary und zeigt den value in prozent an
    gesamt = 0
    for buchstabe in d:
        gesamt = gesamt + d[buchstabe]
    for buchstabe in d:
        d[buchstabe] = round((d[buchstabe] * 100 / gesamt), 2)
    return d

print(prozent(zaehler(text)))



"""text = "das ist ein text um zu testen wie oft jeder buchstabe in ihm vorkommt"

def zaehler2(t): # nimmt einen text und zeigt an wie oft jeder buchstabe vorkommt
    t = sorted(t)
    zaehlung = {}
    for buchstabe in t:
        if buchstabe not in zaehlung:
            zaehlung[buchstabe] = 1
        else:
            zaehlung[buchstabe] = zaehlung[buchstabe] +1
    return zaehlung


def prozent2(d): # nimmt ein dictionary und zeigt den value in prozent an
    gesamt = 0
    for buchstabe in d:
        gesamt = gesamt + d[buchstabe]
    for buchstabe in d:
        d[buchstabe] = d[buchstabe] * 100 / gesamt
        print("{0:>2s} : {1:5.2f}" .format(buchstabe, d[buchstabe]), " " + int(d[buchstabe]) * "x")

print(prozent2(zaehler2(text)))"""

