#program wypisujący liczby od 0 do 20 nippodzielne przez 4
licznik=0
while licznik<21:
    if licznik%4!=0:
        print(licznik," ",end="")
    licznik+=1
for x in range(20):
    if x%4!=0:
        print(x," ",end="")
imiona=["Ania","Basia","Celina"]
for indeks, imie in enumerate(imiona):
    print(f"{indeks}{imie}")

nazwiska=["Duda","Eda","Fuda"]
for imie, nazwisko in zip(imiona,nazwiska):
    print(f"{imie} {nazwisko}")
