Bogsamling = []

class Bog: #Klasse til bøgerne.
    def __init__(self, title, forfatter, genre, isbn, bedømmelse=None, læststatus=None): #Bogen markeres med title, forfatte, genre, ISBN, bedømmelse og læsestatus.
        self.title = title
        self.forfatter = forfatter
        self.genre = genre
        self.isbn = isbn
        self.bedømmelse = bedømmelse
        self.læststatus = læststatus


class Bibliotek: #Klasse til biblioteket for bog samlingen.
    def __init__(self):
        self.bøger = [
            Bog("Vaskebjørns Teorien","Ukendt","Kunst litteratur","1717171717171",10,"læst"), #Dummy bøger der er registret på forhånd.
            Bog("Guide til LUA", "Jacob Pedersen", "Guide", "1234567893923", 7, "ulæst"),
            Bog("Jens fryser", "Jensen", "horror", "1284567897923", 1, "ulæst"),
            Bog("Grundbog i retorik", "Systime", "horror", "1236567855923", 2, "læst"),
            Bog("Jens går tur", "Jensen", "horror", "1234587886923", 4, "læst"),

        ] #liste til at gemme registreret bøger.


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
                print("Denne bog er ikke registreret og kan derfor ikke bedømmes.")




def bogStatus(): #Funktion til at ændre læse status på bogen.
    RegistrerSvarStatus = input("Vil du ændre statusen af en bog?").upper() #Brugeren bliver spurgt om de vil ændre statusen på en bog.
    if RegistrerSvarStatus == "JA": #Funktion forsætter hvis svaret er ja.
        titel = input("Hvilken bog vil du ændre status på? ").upper() #Gør det muligt at vælge hvilken bog der skal ændre status på.

        for bog in bib.bøger: #Hvis den intastet bog findes i biblioteket over bøger vil man kunne ændre statusen på bogen.
            if bog.title.lower() == titel.lower():
                print("bogen er fundet")
                fundet = True  # Marker at bogen er fundet i biblioteket.

                while True: #En løkke til intastelse af bogens læse status som afbrydes når der regitreres gyldigt input.
                    status = input("Er bogen læst eller ulæst").upper() #Brugeren bliver spurgt om bogen er læst eller ulæst.
                    if status in ("LÆST", "ULÆST"): #Svaret skal være læst eller ulæst.
                        bog.læststatus = status #Bogens status ændres.
                        print("Bogens status er nu ændret") #Meddelse til brugeren om at stausen er ændret.
                        break #Løkken afbrydes.
                    else:
                        print("Bogen skal markeres som læst eller ulæst") #Hvis bogen ikke markeres som læst eller ulæst vil brugeren blive spurgt om at vælge en af valg mulighederne.
                if not fundet: #Hvis bogen ikke findes i biblioteket får brugeren denne meddelse.
                    print("Denne bog er ikke registreret og kan derfor ikke markers som læst eller ulæst")




def bogSearch(): #Funktion der gør det muligt at søge efter en bog ud fra genre, forfatter eller bedømmelse.
    RegistrerSvarSearch = input("Hvad vil du søge efter (genre / forfatter / bedømmelse)?").upper() #Brugeren bliver spurgt om hvad de vil søge efter.

    if RegistrerSvarSearch == "genre".upper(): #Hvis input er genre vil der blive spurgt om hvilken genre.
        genre = input("Hvilken genre? ").upper()
        for bog in bib.bøger: #Hvis den intastet genre findes i biblioteket over bøger, printes der en oversigt over bøger med samme genre.
            if bog.genre.lower() == genre.lower():
                print(f"Bogen {bog.title} af {bog.forfatter}, genre {bog.genre}")

    elif RegistrerSvarSearch == "forfatter".upper(): #Hvis forfatter er genre vil der blive spurgt om hvilken forfatter.
        forfatter = input("Hvilken forfatter? ").upper()

        for bog in bib.bøger: #Hvis den intastet forfatter findes i biblioteket over bøger, printes der en oversigt over bøger med samme forfatter.
            if bog.forfatter.lower() == forfatter.lower():
                print(f"Bogen {bog.title} af {bog.forfatter}, genre {bog.genre}")

    elif RegistrerSvarSearch == "bedømmelse".upper(): #Hvis input er bedømmelse vil der blive spurgt om hvilken bedømmelse.
        try:
            bedømmelse = int(input("Hvilken bedømmelse? ")) #Koden vil prøve at konvertere inputtet til et gyldigt tal.
            for bog in bib.bøger: #Hvis den intastet bedømmelse findes i biblioteket over bøger, printes der en oversigt over bøger med samme bedømmelse.
                if int(bog.bedømmelse) == bedømmelse:
                    print(f"Bogen {bog.title} af {bog.forfatter}, genre {bog.genre}")
        except ValueError: #Søger for at koden ikke crasher hvis inputet ikke kan konverteres til et heltal.
            print("Bedømmelsen skal være et tal.") #Meddeler brugeren om at de skal skrive et gyldigt tal.
    else:
        print("ugyldigt valg. Prøv igen.") #Hvis der ikke intastes en af valg mulighederne gives denne meddelse.


registrereBog()
bogBedømmelse()
bogStatus()
bogSearch()




