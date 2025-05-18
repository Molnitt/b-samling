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
    if RegistrerSvar == "JA": #Hvis "Ja" vil der blive spurgt om bog information som title genre og forfatter..
        title = input("Hvilken bog vil du registrere? ")
        forfatter = input("Hvem er forfatteren af bogen? ")
        genre = input("Hvilken genre har bogen? ")

        while True: #En løkke til intastelse af ISBN kode som afbrydes når der regitreres gyldigt input.
            isbn = input("Hvad er bogens ISBN? (13 cifre) ")
            if isbn.isdigit() and len(isbn) == 13: #Tjekkes for om den intastet ISBN kode består af tal og er 13 cifre lang.
                break #Løkken afbrydes.
            else:
                print("Ugyldigt ISBN, prøv igen") #Hvis den intastet ISBN ikke er 13 cifre eller indholder bogstaver, vil der være fejl og man vil skulle intaste den igen.

        ny_bog = Bog(title, forfatter, genre, isbn) #Opretter bogen med de angivet oplysninger.
        bib.tilføj(ny_bog) #Bog tilføjet til bibliotek
        print("Denne bog er nu registreret") #Meddelse til brugeren om at bogen er registreret.




def bogBedømmelse(): #Funktion der gør det muligt at ændre bedømmelsen på bøger.
    RegistrerSvarBedømmelse = input("Vil du bedømme en bog?").upper() #Brugeren bliver spurgt om de vil bedømme en bog.
    if RegistrerSvarBedømmelse == "JA": #Funktionen forsætter hvis der svares ja.
        titel = input("Hvilken bog vil du bedømme?").upper() #Brugeren bliver spurgt om bogens title.

        fundet = False #Variable til at holde øje med om bogen er fundet i biblioteket.

        for bog in bib.bøger: #Hvis den intastet bog findes i biblioteket over bøger vil man kunne bedømme bogen.
            if bog.title.lower() == titel.lower():
                print("bogen er fundet")
                fundet = True #Marker at bogen er fundet i biblioteket.

                while True: #En løkke til intastelse af bogens bedømmelse som afbrydes når der regitreres gyldigt input.
                    try:
                        bedømmelse = int(input("Hvordan vil du bedømme bogen fra 1-10?"))  #Brugeren bliver spurgt om hvordan de vil bedømme bogen fra 1-10.

                        if 1 <= bedømmelse <= 10: #Der tjekkes om svaret ligger i intervallet fra 1-10.
                            bog.bedømmelse = bedømmelse #Bogens bedømmelse ændres.
                            print("Bogens bedømmelse er nu ændret") #Meddelse til brugeren om at bogens bedømmelse er nu ændret.
                            return
                        else:
                            print("Vælg et tal fra 1-10") #Gøre brugeren opmærksom på at koden skal være et tal fra 1-10.
                    except ValueError: #Søger for at koden ikke crasher hvis inputet ikke kan konverteres til et heltal.
                        print("Skriv et valideret tal")
                    break #løkken afsluttes.
            if not fundet: #Hvis bogen ikke findes i bibliotekket vil den printe teksten nedenfor.
                print("Denne bog er ikke registreret og derfor ikke bedømmes.")




def bogStatus(): #Funktion til at ændre læse status på bogen.
    RegistrerSvarStatus = input("Vil du ændre statusen af en bog?").upper() #Brugeren bliver spurgt om de vil ændre statusen på en bog.
    if RegistrerSvarStatus == "JA": #Funktion forsætter hvis svaret er ja.
        titel = input("Hvilken bog vil du ændre status på? ").upper() #Gør det muligt at vælge hvilken bog der skal ændre status på.

        for bog in bib.bøger: #Hvis den intastet bog findes i biblioteket over bøger vil man kunne ændre statusen på bogen.
            if bog.title.lower() == titel.lower():
                while True: #En løkke til intastelse af bogens læse status som afbrydes når der regitreres gyldigt input.
                    status = input("Er bogen læst eller ulæst").upper() #Brugeren bliver spurgt om bogen er læst eller ulæst.
                    if status in ("LÆST", "ULÆST"): #Svaret skal være læst eller ulæst.
                        bog.læststatus = status #Bogens status ændres.
                        print("Bogens status er nu ændret") #Meddelse til brugeren om at stausen er ændret.
                        break #Løkken afbrydes.
                    else:
                        print("Bogen skal markeres som læst eller ulæst") #Hvis bogen ikke markeres som læst eller ulæst vil brugeren blive spurgt om at vælge en af valg mulighederne.
        print("Denne bog er ikke registreret og kan derfor ikke markeres med status.") #Hvis bogen ikke kan findes i biblioteket kan dens status ikke ændres.

registrereBog()
bogBedømmelse()
bogStatus()




