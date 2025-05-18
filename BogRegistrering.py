Bogsamling = []

class Bog: #Klasse til bøgerne.
    def __init__(self, title, forfatter, genre, isbn, bedømmelse=None, læststatus=None):
        self.title = title
        self.forfatter = forfatter
        self.genre = genre
        self.isbn = isbn
        self.bedømmelse = bedømmelse
        self.læststatus = læststatus

    def __str__(self):
        return "'{self.title}' af {self.forfatter} | Genre: {self.genre} | Bedømmelse: {self.bedømmelse} | Status: {self.læststatus}"


class Bibliotek:
    def __init__(self):
        self.bøger = []

    def tilføj(self, bog):
        self.bøger.append(bog)


bib = Bibliotek()


def registrereBog(): #Funktion der gør at man kan ændre statusen på bøger.
    RegistrerSvar = input("Vil du registrere en bog? ").upper() #Man får valget om man vil registrer en bog eller ej.
    if RegistrerSvar == "JA": #Hvis "Ja" vil
        title = input("Hvilken bog vil du registrere? ")
        forfatter = input("Hvem er forfatteren af bogen? ")
        genre = input("Hvilken genre har bogen? ")

        while True:
            isbn = input("Hvad er bogens ISBN? (13 cifre) ")
            if isbn.isdigit() and len(isbn) == 13: #Tjekkes for om den intastet ISBN kode består af tal og er 13 cifre lang.
                break
            else:
                print("Ugyldigt ISBN, prøv igen") #Hvis den intastet ISBN ikke er 13 cifre eller indholder bogstaver, vil der være fejl og man vil skulle intaste den igen.

        ny_bog = Bog(title, forfatter, genre, isbn) #Opretter bogen med de angivet oplysninger.
        bib.tilføj(ny_bog) #Bog tilføjet til bibliotek
        print("Denne bog er nu registreret") #Meddelse til brugeren om at bogen er registreret.

registrereBog()
print(bib.bøger)


def bogBedømmelse(): #Funktion der gør det muligt at ædre bedømmelsen på bøger.
    RegistrerSvarBedømmelse = input("Vil du bedømme en bog?").upper()
    if RegistrerSvarBedømmelse == "JA":
        titel = input("Hvilken bog vil du bedømme?").upper()

        fundet = False
        for bog in bib.bøger: #Hvis den intastet bog findes i biblioteket over bøger vil man kunne bedømme bogen.
            if bog.title.lower() == titel.lower():
                print("bogen er fundet")
                bedømmelse = int(input("Hvordan vil du bedømme bogen fra 1-10?"))
                bog.bedømmelse = bedømmelse #Bogens bedømmelse ændres.
                print("Bogens bedømmelse er nu ændret")
                fundet = True
                break

        if not fundet: #Hvis bogen ikke findes i bibliotekket vil den printe teksten nedenfor.
            print("Denne bog er ikke registreret og derfor ikke bedømmes.")

bogBedømmelse()
print(bib.bøger)


def bogStatus(): #Funktion til at ændre status på bogen.
    RegistrerSvarStatus = input("Vil du ændre statusen af en bog?").upper()
    if RegistrerSvarStatus == "JA":
        titel = input("Hvilken bog vil du ændre status på? ").upper() #Gør det muligt at vælge hvilken bog der skal ændre status på.

        fundet = False #Hvis bogen findes i biblioteket vil man få valget mellem at bogen er læst eller ulæst.
        for bog in bib.bøger:
            if bog.title.lower() == titel.lower():
                status = input("Er bogen læst eller ulæst").upper()
                bog.læststatus = status #Bogens status ændres
                print("Bogens status er nu ændret")
                fundet = True

        if not fundet: #Hvis bogen ikke kan findes i biblioteket kan der ikke ændres status.
            print("Denne bog er ikke registreret og kan derfor ikke markeres med status.")

bogStatus()
print(bib.bøger)





