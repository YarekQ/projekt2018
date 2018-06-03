zaklista=["piwo","kiełbasa","węgiel","piwo"]
print(zaklista)
#listy są mutowlane
zaklista[2]="reds"
print(zaklista[:2])
zaklista.append("wykałaczki")
drugalista=["więcej piwa","wiecej kiełbasy"]
print(zaklista)
print(zaklista+drugalista)
#dodawanie elementu
zaklista.insert(1,"gwizdek")
print(zaklista)
#usuwanie elementu (ale musi być w zbiorze)
zaklista.remove("piwo")
print(zaklista)
if "piwo" in zaklista:
    zaklista.remove("piwo")
print(zaklista)
#usuwanie po indeksie
del zaklista[3]
#usuwanie popem
niepotrzebny=zaklista.pop(2)
print(niepotrzebny)
print(zaklista)