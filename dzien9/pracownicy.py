from dzien9.pracownik import Pracownik

pracownik1=Pracownik("Johny",123456789,"monter")
pracownik2=Pracownik("Zenek",70062608298,"szef")
pracownik3=Pracownik("Rysiek",75062304960,"brygadzista")


print(pracownik1)
print(pracownik2)
print(pracownik3)

pracownik1.ustalpensje()
pracownik2.ustalpensje()
pracownik3.ustalpensje()

print(pracownik1)
print(pracownik2)
print(pracownik3)

print(f"pracowników w pracy: {Pracownik.iloscpracownikow}")
del pracownik3
print(f"pracowników w pracy: {Pracownik.iloscpracownikow}")