#słownik=jeden element to klucz+wartość
#klucze musza byc niemutowalne, wartości-dowolne
x={"nazwisko":"Kowalski","pesel":70062608298}
print(x["pesel"])
#albo
osoby={"studenci":["Ala","Basia","Celina"],"wykładowcy":["profesor",'doktor']}
osoby["wykładowcy"].append("magister")
osoby.update({"ochrona":"impel"})

print(osoby)