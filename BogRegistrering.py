Bogsamling = []

class Bog: #Klasse til bøgerne.
    def __init__(self, title, forfatter, genre, isbn, bedømmelse=None, læststatus=None): #Bogen markeres med title, forfatte, genre, ISBN, bedømmelse og læsestatus.
        self.title = title
        self.forfatter = forfatter
        self.genre = genre
        self.isbn = isbn
        self.bedømmelse = bedømmelse
        self.læststatus = læststatus

    def __str__(self):
        return "'{self.title}' af {self.forfatter} | Genre: {self.genre} | Bedømmelse: {self.bedømmelse} | Status: {self.læststatus}"


class Bibliotek: #Klasse til biblioteket for bog samlingen.
    def __init__(self):
        self.bøger = [] #liste til at gemme registreret bøger.

    def tilføj(self, bog):
        #Tilføjer bøger til biblioteket.
        self.bøger.append(bog)

#Opretter bibliotek-objekt.
bib = Bibliotek()




def registrereBog(): #Funktion til at registre bøger.
    RegistrerSvar = input("Vil du registrere en bog? ").upper() #Man får valget om man vil registrer en bog eller ej.
    if RegistrerSvar == "JA": #Hvis "Ja" vil der blive spurgt om bog info.
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




def bogBedømmelse(): #Funktion der gør det muligt at ændre bedømmelsen på bøger.
    RegistrerSvarBedømmelse = input("Vil du bedømme en bog?").upper()
    if RegistrerSvarBedømmelse == "JA":
        titel = input("Hvilken bog vil du bedømme?").upper()

        for bog in bib.bøger: #Hvis den intastet bog findes i biblioteket over bøger vil man kunne bedømme bogen.
            if bog.title.lower() == titel.lower():
                print("bogen er fundet")
                while True:
                    try:
                        bedømmelse = int(input("Hvordan vil du bedømme bogen fra 1-10?"))
                        if 1 <= bedømmelse <= 10:
                            bog.bedømmelse = bedømmelse #Bogens bedømmelse ændres.
                            print("Bogens bedømmelse er nu ændret")
                            return
                        else:
                            print("Vælg et tal fra 1-10")
                    except ValueError:
                        print("Skriv et valideret tal")
                    break
            if not fundet: #Hvis bogen ikke findes i bibliotekket vil den printe teksten nedenfor.
                print("Denne bog er ikke registreret og derfor ikke bedømmes.")




def bogStatus(): #Funktion til at ændre læse status på bogen.
    RegistrerSvarStatus = input("Vil du ændre statusen af en bog?").upper()
    if RegistrerSvarStatus == "JA":
        titel = input("Hvilken bog vil du ændre status på? ").upper() #Gør det muligt at vælge hvilken bog der skal ændre status på.

        for bog in bib.bøger:
            if bog.title.lower() == titel.lower():
                while True:
                    status = input("Er bogen læst eller ulæst").upper()
                    if status in ("LÆST", "ULÆST"):
                        bog.læststatus = status #Bogens status ændres
                        print("Bogens status er nu ændret")
                        return
                    else:
                        print("Bogen skal markeres som læst eller ulæst")
        print("Denne bog er ikke registreret og kan derfor ikke markeres med status.")

registrereBog()
bogBedømmelse()
bogStatus()




