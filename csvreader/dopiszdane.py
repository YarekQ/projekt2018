import csv
def dopisz(plikzdanymi,baza):
    """
    funkcja dopisuje nie zapisane wcześniej rekordy do bazy danych
    :param lista:
    :param baza:
    :return: nic (aktualizuje bazę)
    """
    with open(plikzdanymi,"r") as file:
        reader = csv.reader(file)
        for line in reader:
            if line not in baza:
                baza.append(line)
    print(f"dopisano dane z pliku: {plikzdanymi}\n")