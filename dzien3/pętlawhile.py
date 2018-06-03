licznik=0
while licznik<4:
    licznik+=1
    print(f"Licznik={licznik}")
zakupy=["piwo","kiełbasa","cebula","sok","ryba","karkówka"]
listam=("masło","majonez","mkleko","mąka")
ilość=zakupy.count("piwo")

for indeks, produkt in enumerate(zakupy):
    print(f"{indeks},{produkt}")
print(ilość)
for indeks, produkt in enumerate(listam):
    print(f"{indeks},{produkt}")
#dodawanie na końcu
zakupy.append("coś do picia dla dzieci")
for indeks, produkt in enumerate(zakupy):
    print(f"{indeks},{produkt}")
#usuwanie elementu po nazwie
zakupy.remove("ryba")
for indeks, produkt in enumerate(zakupy):
    print(f"{indeks},{produkt}")
#usuwanie ntego elementu
zakupy.pop(2)
for indeks, produkt in enumerate(zakupy):
    print(f"{indeks},{produkt}")
#dodawanie list
nowezakupy=["musztarda","sos czosnkowy","tysiąc wysp"]
zakupy=zakupy+nowezakupy
for indeks, produkt in enumerate(zakupy):
    print(f"{indeks} {produkt}")


