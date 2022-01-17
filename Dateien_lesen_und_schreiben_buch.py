with open("datei_programmieren.txt", "r+", encoding="utf-8") as datei:
    for line in datei:
        print(line, end="")
    print("")
datei.close()

# Encoding sollte das Encoding des file matchen, anderweitig gibt es Fehler / Fehloutput

# Beispiel für tell
with open("datei_programmieren.txt", "r+", encoding="utf-8") as datei:
    datei.seek(0)
    line = "PLACEHOLDER"
    while line != "":
        print(datei.tell(), end=" ")
        line = datei.readline()
        print(line)

datei.close()

# Path Objekte aus pathlib lassen sich seit 3.6 auch als Ziel für open angeben
# auch in früheren Versionen lässt sich pathlib verwenden, jedoch muss der Pfad zuerst zum String umgewandelt werden


#DATEIEN MIT WITH/AS AUTOMATISCH SCHLIESSEN

# wenn Dateien mit with/as geöffnet werden, schliessen sie am Ende des Blocks automatisch. close wird nicht gebraucht.
# Um sicherzustellen das die Datei geschlossen wird, kann man folgendes Muster verwenden:
"""try:
    f = open("Dateiname")
finally:
    f.close()"""

# Man kann auch mehrere Dateien gleichzeitig öffnen:

"""with open("datei1") as dat1, open("datei2") as dat2:
    pass"""

# with/as schützt nicht vor exceptions
"""
try:
    f = open("Dateiname")
except OSError:
    print("Dateiname falsch!")
finally:
    f.close()"""

# INDEXEINTRÄGE IN TEXTDATEIEN ÄNDERN

# BEISPIEL "Indexeinträge modifizieren"
# der folgende Code liest alle Dateien mit Endung .md ein, und führt diese durch eine transform funktion
# diese funktion gibt zeilen die keine indexeinträge enthalten unverändert zurück
# und verändert alle Zeilen mit indexeinträgen um der neuen Formattierung zu genügen

# Beispieldatei repair-index.py
from pathlib import Path

# eine Zeile auswerten, gegebenenfalls \index-Eintrag
# ändern und zurückgeben
def transform(s):
    # wenn kein Indexeintrag: unverändert zurückgeben
    if not s.startswith(r"\index{"):
        return s

    # \index{*-Funktion/Methode/Variable/....}
    keywords = ['Funktion', 'Methode', 'Variable']
    for word in keywords:
        if '-' + word + '}' in s:
            new = s.replace('-' + word, ' (' + word + ')')
            print(' - ', s, ' + ', new, end="", sep="")
            return new
    # Sonderfall \index{*-Modul}
    if '-Modul' in s:
        pos = s.find('-Modul')
        new1 = r'\index{Modul!' + s[7:pos] + '}\n'
        new2 = s.replace('-Modul', ' (Modul)')
        print(' - ', s, ' + ', new1, ' + ', new2, end="", sep="")
        return new1 + new2
    # sonstiger Indexeintrag unverändert lassen
    return s



# Schleife über alle *.md-Dateien
"""for currentPath in Path.cwd().glob('*.md'):
    print("\nBearbeite", currentPath.name)
    # Backup erstellen
    bak = currentPath.with_suffix('.bak')
    currentPath.rename(bak)     # benennt DATEI um, nicht Pfad
    #Backup lesen, in neue *.md-Datei schreiben
    with open(bak, 'rt') as fin, \
        open(currentPath, 'wt') as fout:
        #Datei zeilenweise verarbeiten
        for line in fin:
            fout.write(transform(line))"""

