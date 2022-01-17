#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import QSize    
SCREEN_X = 405//8*7
SCREEN_Y = 720//8*7


class Tisch:
    def __init__(self, tischnummer, name):
        self.tischnummer = tischnummer
        self.name = name
        self.artikelanzahl = 0
        self.saldo = 0

def tisch_öffnen(n):
    for tisch in restaurant:
        if tisch.tischnummer == n:
            return tisch


class MyWindow(QMainWindow):
    def __init__(self,restaurant):
        # Konstruktor von QMainWindow aufrufen
        super().__init__()

        # Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(SCREEN_X, SCREEN_Y))
        self.setWindowTitle('laccordo')
        self.presentationbuttonlist = []

        pos = 0
        for t in restaurant:
            b4 = QPushButton(f"{t.tischnummer:<40} {t.name} {t.saldo:>40} €", self)
            b4.move(0, pos)
            b4.resize(SCREEN_X, SCREEN_X // 4)
            b4.clicked.connect(self.tischinhalt)
            self.presentationbuttonlist.append(b4)
            pos += SCREEN_X // 4

        # Button-Widgets erzeugen und in Fenster einbetten
        knöpfe = []
        x = 0
        y = SCREEN_Y - SCREEN_X
        for i in range(1, 13):
            if i == 10:
                text = "c"
            elif i == 11:
                text = "0"
            elif i == 12:
                text = "<<"
            else:
                text = str(i)
            b1 = QPushButton(text, self)
            b1.move(x, y)
            b1.resize(SCREEN_X // 4, SCREEN_X // 4)
            b1.clicked.connect(self.tastaturknopf)
            x += SCREEN_X // 4
            if x == SCREEN_X // 4 * 3:
                y += SCREEN_X // 4
                x = 0

        
        b2 = QPushButton('Tisch', self)
        b2.move(SCREEN_X//4*3, SCREEN_Y - SCREEN_X//2)
        b2.resize(SCREEN_X//4, SCREEN_X//2)
        b2.clicked.connect(self.tischknopf)

        b3 = QPushButton('BB', self)
        b3.move(SCREEN_X // 4 * 3, SCREEN_Y - SCREEN_X)
        b3.resize(SCREEN_X // 4, SCREEN_X // 2)
        b3.clicked.connect(self.tischknopf)

    def tastaturknopf(self):
        global user_input
        c = self.sender()
        user_input += c.text()
    
    def tischknopf(self):
        t = tisch_öffnen(int(user_input))

    def tischinhalt(self):
        pass




restaurant = [Tisch(i, "Tisch") for i in range(1,5)]

# Fenster öffnen; das Programm läuft, bis das
# Fenster geschlossen wird
user_input = ""
app = QtWidgets.QApplication([])
win = MyWindow(restaurant)
win.show()
app.exec_()


