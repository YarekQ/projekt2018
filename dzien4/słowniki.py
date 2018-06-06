x={1:"Ola",2:"Ala",3:"Ela"}
print(x[1])

#słonikmozna stworzycrównieżtak:
zakupy={}
zakupy["Chemia"]=["płyn","żel"]
zakupy["Jedzenie"]=["ser","mleko"]

print(zakupy)
for k in zakupy.keys():
    print(k)
for v in zakupy.values():
    print(v)
for klucz, wart in zakupy.items():
    print(f"klucz={klucz} wartość={wart}")
#jeden element
print(zakupy["Chemia"][0])