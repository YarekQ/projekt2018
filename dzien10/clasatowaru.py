class Towar(object):

    def __init__(self,nazwa,kolor,cena):
        self.nazwa=nazwa
        self.kolor=kolor
        self.cena=cena
    def __str__(self):
        return f"{self.nazwa.capitalize}, {self.kolor.capitalize} {self.cena}"
    def __add__(self, other):
        wartosc=self.cena + other.cena
        return wartosc

t1 = Towar("krzeslo","braz",340)
t2 = Towar("stol","braz",30)
t3 = Towar("fotel","blekit",1250)

wartosc=0

sklep=[t1,t2,t3]

for przedmiot in sklep:
    wartosc=wartosc + przedmiot
print(wartosc)
print(t1+t2)


if __name__ == '__main__':
    main()