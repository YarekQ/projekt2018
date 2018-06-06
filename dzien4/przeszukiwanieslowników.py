from pprint import pprint
gwiazdy={}
gwiazdy[1]={"imie":"John","nazwisko":"Turturo","stawka":100,"status":"retired"}
print(gwiazdy[1])
gwiazdy[2]={"imie":"John","nazwisko":"Travolta","stawka":200,"status":"still alive"}
pprint(gwiazdy)

#szukanie

poszukiwany="John Travolta"

for pracownik in gwiazdy.values():
    if pracownik[imie]+" "+pracownik[nazwisko]==poszukiwany:
        print(f"poszukiwany ma stawkę {pracownik[stawka]}")