def hi(imie):
    print(f"Cześć {imie.title()}")
imie="zenek"
hi(imie)
hi("Baśka")

def drukuj(znak,ilosc):
    """
    :param znak: rodzaj zmiennej, co robi
    :param ilosc: rodzaj zmiennej, co robi
    :return: (co zwraca)
    """
    for i in range(ilosc):
        print(znak, end="")
drukuj("s",16)
#zliczanie znaków w zdaniu
def licz(litera,zdanie):
    answer=zdanie.count(litera)
    print(answer)
    odwr=zdanie.capitalize()
    return (answer)

licz("a", "baba")
print(licz("a","Agata nogą zamiata"))

#tworzenie docstringów (documentacji)
def licz(litera,zdanie):
    """"docstring ma byc tutaj
    program manipuluje stringami
    """
    answer=zdanie.count(litera)
    print(answer)
    odwr=zdanie.capitalize()
    print(odwr)
licz("a", "baba")