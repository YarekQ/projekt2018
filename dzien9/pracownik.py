class Pracownik(object):

    zarobki={"monter":1000,"szef":2000,"brygadzista":1500}
    iloscpracownikow=0

    def __init__(self, imie, pesel, stanowisko,):
        self.imie=imie
        self.stanowisko=stanowisko
        self.pensja=Pracownik.zarobki
        self.pesel=pesel

        Pracownik.iloscpracownikow +=1

    def __str__(self):
        return f"Pracownik {self.imie} na stanowisku {self.stanowisko} ma pensję {self.pensja}"

    def ustalpensje(self):
        if self.stanowisko=="monter":
            self.pensja=1000
        if self.stanowisko=="szef":
            self.pensja=2000
        if self.stanowisko=="brygadzista":
            self.pensja=1500

    def __del__(self):
        Pracownik.iloscpracownikow -= 1
        print("usunięto pracownika")


