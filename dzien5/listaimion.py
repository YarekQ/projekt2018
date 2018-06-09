#drugi argument jest opcjonalny

def dodajimie (imie: str, imiona=[]):
    imiona.append(imie.capitalize())
    return imiona
anglicy=dodajimie("John")
anglicy=dodajimie("Paul")

print(anglicy)

polacy=dodajimie("Janek")

print(anglicy)
print(polacy)

