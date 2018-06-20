from dzien10.towar import Towar
class AGD(Towar):
    def __init__(self,nazwa,producent,cena,typ):
        self.typ=typ
        #inicjowanie z klasy rodzica:
        super().__init__(nazwa,producent,cena)
    def wlacz(self):
        if not self.wlaczony:
            wlaczony=True

def main():
    lod1=(AGD("Lodówka","LG",1700))
    mikser=(AGD("Lodówka","Zelmer",300))

if __name__=="main":
    main()

agd=[lod1,mikser]

print(agd[0])
print(agd[1])