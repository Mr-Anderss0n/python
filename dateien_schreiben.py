
"""with open("datei_programmieren.txt", "w") as datei:
    for i in range(5):
        datei.write("print(\"hello world\")\n")
datei.close()

with open("datei_programmieren.txt", "r") as datei:
    text = datei.read()
    exec(text)
datei.close()"""

"""
with open("datei_programmieren.txt", "r+") as datei:
    for i in range(5):
        datei.write("print(\"hello world\")\n")
    datei.seek(0)
    text = datei.read()
    exec(text)
datei.close()
"""
"""
with open("datei_programmieren.txt", "r+") as datei:
    datei.seek(len("print(\"hello world\")\n"))
    for i in range(5):
        datei.write("print(\"hello world\")\n")
    datei.seek(0)
    text = datei.read()
    exec(text)
datei.close()
"""


with open("datei_programmieren.txt", "r+". encoding="utf-8") as datei:
    text = datei.read()
    datei.seek(0)
    n = 0
    for i, character in enumerate(text):
        if character == "\n":
            n += 1
        if n == 4:
            break
    datei.seek(i+3)
    for i in range(5):
        datei.write("print(\"hello world\")\n")
    datei.seek(0)
    text = datei.read()
    exec(text)
datei.close()