import pickle

database=[]

def otworz(plik,tryb):
    """
    funkcja otwiera bazę danych z podanej lokalizacji
    baza zapisana uprzednio za pomocą pickle

    :param plik: scieżka i nazwa pliku
    :param tryb: odczyt binarny
    :return: lista rekordów
    """
    with open(plik,tryb) as plik:
        database = pickle.load(plik, encoding='utf-8')
    print(f"znaleziono i otwarto bazę danych ({len(database)-1} transakcji)")
    return database