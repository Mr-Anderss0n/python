import random

class Node:
    def __init__(self, value):
        self.value = value
        self.R = None
        self.L = None

    def drunter_einfuegen(self, value):
        if value == self.value:
            return
        if value < self.value:
            self.einfügen_rechts(value)
        else:
            self.einfügen_links(value)


    def einfügen_rechts(self, value):
        if self.R:
            self.R.drunter_einfuegen(value)
        else:
            self.R = Node(value)



    def einfügen_links(self, value):
        if self.L:
            self.L.drunter_einfuegen(value)
        else:
            self.L = Node(value)

    def ausgabe(self):
        if self.R:
            self.R.ausgabe()
        print(self.value, end=", ")
        if self.L:
            self.L.ausgabe()

    def finden(self, value):
        if self.value == value:
            return True
        if value < self.value and self.R != None:
            containedInRightSubtree = self.R.finden(value)
            return containedInRightSubtree
        elif value < self.value:
            return False
        if value > self.value and self.L != None:
            containedInLeftSubtree = self.L.finden(value)
            return containedInLeftSubtree
        elif value > self.value:
            return False



root = Node(6)
for i in [4,8,9,5]:
    root.drunter_einfuegen(i)
print(root.finden(7))

