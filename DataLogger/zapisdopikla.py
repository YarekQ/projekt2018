import pickle


def zapiszdopikla(nazwapliku,dane):
    with open(nazwapliku,"wb") as plik:
        pickle.dump(dane,plik)

def odczytajzpikla(nazwapliku):
    with open(nazwapliku,"rb") as plik2:
        nowalista=pickle.load(plik2,encoding="utf-8")
        return nowalista

if __name__ == '__main__':
    pickle
