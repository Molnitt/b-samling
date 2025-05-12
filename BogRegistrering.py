Bogsamling = []

class Bog:
    def __init__(self, title, forfatter, genre, isbn, bedømmelse=None, læststatus=None):
        self.title = title
        self.forfatter = forfatter
        self.genre = genre
        self.isbn = isbn
        self.bedømmelse = bedømmelse
        self.læststatus = læststatus



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

def bogBedømmelse():
    titel = input("Hvilken bog vil du bedømme?").upper()

    fundet = False
    for bog in bib.bøger:
        if bog.title.lower() == titel.lower():
            bedømmelse = input("Hvordan vil du bedømme bogen fra 1-10?").upper()
            bog.bedømmelse = bedømmelse
            print("Bogens bedømmelse er nu ændret")
            fundet = True
            break
    if not fundet:
        print("Denne bog er ikke registreret og derfor ikke bedømmes.")

bogBedømmelse()
print(bib.bøger)



def bogStatus():
    titel = input("Hvilken bog vil du ændre status på? ").upper() #Gør det muligt at vælge hvilken bog der skal ændre status på.

    fundet = False #Hvis bogen findes i biblioteket vil man få valget mellem at bogen er læst eller ulæst.
    for bog in bib.bøger:
        if bog.title.lower() == titel.lower():
            status = input("Er bogen læst eller ulæst").upper()
            bog.læststatus = status
            print("Bogens status er nu ændret")
            fundet = True
            break
    if not fundet: #Hvis bogen ikke kan findes i biblioteket kan der ikke ændres status.
        print("Denne bog er ikke registreret og kan derfor ikke markeres med status.")


bogStatus()
print(bib.bøger)



#def bedømmelseSystem():
   # BedømmelseSvar = input("Vi du bedømme en tidligere regristreret bog?").upper()
   # if BedømmelseSvar == "JA":
       # bogvalg = input("Hvilken bog?")


