from datetime import datetime

def setReleaseDate():
    # Aufgabe 2
    day = int(input("Tag: "))
    month = int(input("Monat: "))
    year = int(input("Jahr: "))

    return datetime(year, month, day)

def addBookToShelf(listOfBooks):
    # Aufgabe 1
    # Aufgabe 2
    newBook = dict()

    newBook["author"] = input("Autor: ")
    newBook["title"] = input("Buchtitel: ")
    newBook["pages"] = int(input("Seitenanzahl: "))
    newBook["price"] = float(input("Verkaufspreis: "))

    newBook["release"] = setReleaseDate()

    listOfBooks.append(newBook)

def printTitles(listOfBooks):
    # Aufgabe 3
    for book in listOfBooks:
        line = book["author"]
        line += ": "
        line += book["title"]
        line += " ("
        line += str(book["release"].year)
        line += ")"

        print(line)

def findOlderBooks(listOfBooks):
    # Aufgabe 4
    for book in listOfBooks:
        if book["release"].year < 2000:
            line = book["author"]
            line += ": "
            line += book["title"]

            print(line)

def sellBook(listOfBooks):
    # Aufgabe 5
    price = float(input("Kaufpreis: "))

    for book in listOfBooks:
        if book["price"] == price:
            line = book["title"]
            line += " wurde verkauft."

            print(line)

            listOfBooks.remove(book)

            return

    print("Es wurde kein Buch für diesen Preis gefunden.")



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
sellBook(bookList)
