from operacje import dtransakcje, utransakcje,statystyka

print("Statystyka transakcji")

opcje = """Wybór:
A - dodaj transakcję
D - usuń transakcję
S - statystyka
Q - Quit"""

wybor = None

while wybor != 'Q':
    print(opcje)
    wybor = input('Twój wybór: ').upper()
    if wybor == 'A':
        transakcja = input("transakcja: ")
        dtransakcje()