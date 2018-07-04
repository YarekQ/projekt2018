class Auto(object):
    def __init__(self,kolor,klima,marka):
        self.producent=marka
        self.klima=klima
        self.kolor=kolor
        self.silnik=None
        self.nachodzie=False
        self.running=False
        self.__przebieg=None
    @property
    def przebieg(self):
        if self.__przebieg==None:
            return 0
        else:
            return "1M"
    @przebieg.setter
    def przebieg(self,newvalue):
        if self.__przebieg>1000000:
            self.__przebieg=self.__przebieg*0.001

    def napraw(self):
        if self.nachodzie:
            print("nie wymaga naprawy, już na chodzie")
            self.nachodzie=True
        else:
            print("naprawiony, już na chodzie")
            self.nachodzie=True

    def switchon(self):
        if self.silnik==None:
            print("sorry - no engine")
        else:
            print("engine running")
            self.silnik="unknown"
            self.running=True

    def switchoff(self):
        if self.silnik==None:
            print("sorry - no engine")
        else:
            print("engine off")
            self.running=False
    def mount(self,model):
        self.silnik=model

    def __str__(self):
        return f"marka={self.producent} jest klima={self.klima} kolor={self.kolor} nachodzie={self.nachodzie} silnik={self.silnik}"
