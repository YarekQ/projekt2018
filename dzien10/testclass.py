class MojaKlasa(object):
    def dodaj(self,a,b):
        return a+b
a=MojaKlasa()

x=a.dodaj(2,3)
print(x)
y=a.dodaj
#wywołanie funkcji bez argumentów zwróci adres funkcji:
print(y)
#wywołanie funkcji z argumentami(!) daje wynik funkcji
print(y(4,5))