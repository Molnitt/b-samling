Bogsamling = []

class Bog:
    def __init__(self, title, forfatter, genre, isbn, bedømmelse=None):
        self.title = title
        self.forfatter = forfatter
        self.genre = genre
        self.isbn = isbn
        self.bedømmelse = bedømmelse
        self.læst = False

    def markerLæst(self):
        self.læst = True





class Bibliotek:
    def __init__(self):
        self.bøger = []

    def tilføj(self, bog):
        self.bøger.append(bog)


bib = Bibliotek()


def registrereBog():
    RegistrerSvar = input("Vil du registrere en bog? ").upper()
    if RegistrerSvar == "JA":
        title = input("Hvilken bog vil du registrere? ")
        forfatter = input("Hvem er forfatteren af bogen? ")
        genre = input("Hvilken genre har bogen? ")
        isbn = input("Hvad er bogens ISBN? ")
        ny_bog = Bog(title, forfatter, genre, isbn)
        bib.tilføj(ny_bog)
        print("Denne bog er nu registreret")



registrereBog()
print(bib.bøger)


#def bedømmelseSystem():
   # BedømmelseSvar = input("Vi du bedømme en tidligere regristreret bog?").upper()
   # if BedømmelseSvar == "JA":
       # bogvalg = input("Hvilken bog?")


