eingabe = input("Geben Sie den Dateinamen ein: ")
with open(eingabe, "r") as aufgabe1:
    lst = aufgabe1.readlines()
    for i in range(2, 0, -1):
        print(lst[-i])

aufgabe1.close()