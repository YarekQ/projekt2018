x={1:"Ola",2:"Ala",3:"Ela"}
print(x[1])

#słonikmozna stworzycrównieżtak:
zakupy={}
zakupy["Chemia"]=["płyn","żel"]
zakupy["Jedzenie"]=["ser","mleko","masło","twarożek"]

print(zakupy)
for k in zakupy.keys():
    print("drukujemy klucze:",k)
for v in zakupy.values():
    print("drukujemy wartości",v)
for klucz, wart in zakupy.items():
    print(f"klucz={klucz} wartość={wart}")
for klucz, wartosc in zakupy.items():
    print(f"druk kluczy: {klucz} i wartość(i): {wartosc}")
#wszystkie elementy dla jednego klucza