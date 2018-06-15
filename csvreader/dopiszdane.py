import csv
import os
def dopisz(listaplikowzdanymi,baza):
    """
    funkcja dopisuje nie zapisane wcześniej rekordy do bazy danych
    :param lista:
    :param baza:
    :return: nic (aktualizuje bazę)
    """
    os.chdir(r"C:\Jts")
    for plikzdanymi in listaplikowzdanymi:
        with open(plikzdanymi,"r") as file:
            reader = csv.reader(file)
            for line in reader:
                if line not in baza:
                    baza.append(line)
    print(f"dopisano dane z pliku(ow): {plikzdanymi}\n")