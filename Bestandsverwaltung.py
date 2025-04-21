"""
Project for Chapter 3
Inventory Management (Bestandsverwaltung)
1. Controlled via a loop
2. Has some items already in it
3. The user can add a new item or change the quantity of existing items.
4. The user can print all of the items.
5. The user can delete an item.
6. Uses at least one tuple, one set, and one list
"""

gegenstände = [
    ["Electric Guitar", 5],
    ["Piano", 3],
    ["Clarinet", 4],
    ["Drum Set", 4]
]

artikelNamen = set()
for gegenstand in gegenstände:
    artikelNamen.add(gegenstand[0])

auswahl = ("1: Print all data", "2: Edit a quantity", "3: Add a new item", "4: Delete an item", "5: Quit")

def artikelHinzufügen(artikelName, menge):
    if artikelName in artikelNamen:
        print("Dieser Artikelname ist bereits auf der Liste.")
    else:
        gegenstände.append([artikelName, menge])
        artikelNamen.add(artikelName)
        print(str(gegenstände[len(gegenstände) - 1]) + " hinzugefügt")

def gegenstandLöschen(gegenstandName):
    if gegenstandName in artikelNamen:
        for i in range(len(gegenstände)):
            if gegenstände[i][0] == gegenstandName:
                gegenstände.pop(i)
                break
        artikelNamen.remove(gegenstandName)
        print(gegenstandName + " gelöscht")
    else:
        print("Gegenstand nicht gefunden")

def mengeBearbeiten(sName, iMenge):
    for gegenstand in gegenstände:
        if gegenstand[0] == sName:
            gegenstand[1] = iMenge

def printData():
    for gegenstand in gegenstände:
        print(gegenstand)

def printOptions():
    print("\n\tBestandsverwaltung")
    for option in auswahl:
        print(option)

wahl = 0
while wahl != 5:
    printOptions()
    wahl = int(input("Geben Sie Ihre Auswahl ein (1, 2, 3 usw.): "))
    match wahl:
        case 1:
            printData()
        case 2:
            name = input("Geben Sie den Gegenstand ein, dessen Menge bearbeitet werden soll: ")
            if name in artikelNamen:
                menge = int(input("Neue Menge: "))
                mengeBearbeiten(name, menge)
            else:
                print("Inventarartikel nicht gefunden")
        case 3:
            name = input("Der name von dem neuen Gegenstand: ")
            menge = int(input("Der Menge des neuen Gegenstands: "))
            artikelHinzufügen(name, menge)
        case 4:
            name = input("Der name des zu löschenden Gegenstands: ")
            gegenstandLöschen(name)
        case 5:
            print("Auf Wiedersehen.")
        case _:
            print("Geben Sie entweder 1, 2, 3, 4 oder 5 ein.")

