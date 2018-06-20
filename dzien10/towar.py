class Towar(object):
    def __init__(self,nazwa,producent,cena):
        self.nazwa=nazwa
        self.producent=producent
        self.cena=cena
    def __str__(self):
        return f"{self.nazwa} {self.producent} {self.cena}"
    def __repr__(self):
        return f" {self.nazwa} - {self.cena}"

def main():
    t1 = Towar("krzeslo","braz", 340)
    t2 = Towar("stol", "braz", 30)
    t3 = Towar("fotel","mokka",1250)

if __name__=="main":
    main()
