from datetime import datetime

def setReleaseDate():
    # Aufgabe 2
    pass

def addBookToShelf(listOfBooks):
    # Aufgabe 1
    pass

    # Aufgabe 2

def printTitles(listOfBooks):
    # Aufgabe 3
    pass

def findOlderBooks(listOfBooks):
    # Aufgabe 4
    pass

def sellBook(listOfBooks):
    # Aufgabe 5
    pass

# Testdaten: nehmen Sie in dem folgenden Bereich keine Änderungen vor.
bookList = list()

book = dict()
book["author"] = "Hermann Hesse"
book["title"] = "Der Steppenwolf"
book["pages"] = 277
book["price"] = 10.00
book["release"] = datetime(1927, 6, 1)
bookList.append(book)

book = dict()
book["author"] = "Sebastian Fitzek"
book["title"] = "Elternabend: Kein Thriller"
book["pages"] = 336
book["price"] = 16.99
book["release"] = datetime(2023, 4, 26)
bookList.append(book)

book = dict()
book["author"] = "Flake"
book["title"] = "Heute hat die Welt Geburtstag"
book["pages"] = 352
book["price"] = 13.00
book["release"] = datetime(2018, 10, 24)
bookList.append(book)


# Ab hier können Sie Ihre Funktionen testen.
print("Herzlich willkommen im Buchhaus Rio Parana!")
