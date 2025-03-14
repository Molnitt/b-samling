def RegistrereBog(bogRegristrering):
    RegistrerSvar = input("Vil du registrere en bog? ").upper()
    if RegistrerSvar == "JA":
        title = input("Hvilken bog vil du registrere? ")
        forfatter = input("Hvem er forfatteren af bogen? ")
        genre = input("Hvilken genre har bogen? ")
        isbn = input("Hvad er bogens ISBN? ")

        ny_bog = Bog(title, forfatter, genre, isbn)
        bogRegristrering.tilføj_bog(ny_bog)
        print("Bog er tilføjet til bog samlingen.")
    else:
        print("Intet registreret.")

def ny_bog():





