monety={5:0,2:0,1:0,0.5:0,0.2:0}

zakupy=26.75
banknot=100
reszta=banknot-zakupy
wydano=0
print(f"reszta do wydania {reszta:.2f}PLN")

for moneta in monety.keys():
    if reszta>=moneta:
        ilemonet=reszta//moneta
        monety[moneta]=ilemonet
        wartosc=ilemonet*moneta
        reszta=reszta-wartosc
        wydano=wydano+wartosc
        print(f"{moneta:.2f}PLN wydano {ilemonet} razy")

#do dokończenia