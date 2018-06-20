class PapieryWW(object):
    def __init__(self,kraj,gielda,klasa,rodzaj):
        self.kraj=kraj
        self.gielda=gielda
        self.rodzaj=rodzaj
        self.klasa=klasa
        self.status=None
    def __str__(self):
        return f"{self.kraj} {self.gielda} {self.rodzaj} {self.klasa}"