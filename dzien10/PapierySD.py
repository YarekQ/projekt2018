from dzien10.PapieryWW import PapieryWW
class PapierySD(PapieryWW):
    def __init__(self,short,long,out):
        self.short=None
        self.long=None
        self.out=True
    def buy (self):
        if self.short:
            self.short=False
            self.long=True
            self.out=True
            self.status="Long"
        else:
            self.short=False
            self.long=False
            self.out=False
            self.status="Out/Short"
    def sell (self):
        if self.long:
            self.short=True
            self.long=False
            self.out=False
            self.status="Short"
        else:
            self.short=False
            self.long=False
            self.out=False
            status="Out"
    def __str__(self):
        pass
#rep słuzy do reprezentacji w postaci stringa wewnątrz innych obiektów (bez printa)
    def __repr__(self):
        pass


JNJ=PapieryWW("USA","NYSE","common stock","shares")

print(JNJ)
print(JNJ.status)
JNJ.status="Long"
print(JNJ.status)
JNJ.status="Short"
print(JNJ.status)
new=JNJ.buy
