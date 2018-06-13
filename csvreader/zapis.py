import pickle
def zapisz(database,plik):
    """
    zapis bazy do pickle
    :param database: baza danych
    :param plik: plik z danymi
    :return: nic (zapisuje bazę)
    """
    with open(plik,'bw') as file:
        pickle.dump(database,file)