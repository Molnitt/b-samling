Bogsamling = []

class Bog:
    def __init__(self, title, forfatter, genre, isbn, bedømmelse=None):
        self.title = title
        self.forfatter = forfatter
        self.genre = genre
        self.isbn = isbn
        self.bedømmelse = bedømmelse

class bibliotek:
    def __init__(self):
        self.bøger = []

    def tilføj(self, bog):
        self.bøger.append(bog)



def RegistrereBog(bogRegristrering):
    RegistrerSvar = input("Vil du registrere en bog? ").upper()
    if RegistrerSvar == "JA":
        title = input("Hvilken bog vil du registrere? ")
        forfatter = input("Hvem er forfatteren af bogen? ")
        genre = input("Hvilken genre har bogen? ")
        isbn = input("Hvad er bogens ISBN? ")


        Bog(title, forfatter, genre, isbn)

        print("Bog er tilføjet til bog samlingen.")
    else:
        print("Intet registreret.")
