import pprint
def drukuj(database):
    """
    funkcja selektywnego przeglądu bazy danych
    :param database:
    :return: nic (wydruk)
    """
    underlyings=[]
    securities=[]
    exchanges=[]

    for line in range(0, len(database)):
        if database[line][0] not in underlyings:
            underlyings.append(database[line][0])
        if database[line][1] not in securities:
            securities.append(database[line][1])
        if database[line][11] not in exchanges:
            exchanges.append(database[line][11])
    print(f"znaleziono dane dla transakcji:\nunderlying:{underlyings[1:]}\nsecurities: {securities[1:]}\nexchanges: {exchanges[1:]}\n")

def filtruj(database,cos):
    """
    wydruk transakcji z zadanym parametrem
    :param database:
    :param cos: szukany string
    :return: nic (wydruk)
    """
    # wydruk nagłówka
    print(f"wydruk transakcji dla wartości filtra: {cos}\n")
    print(f"{database[0][0]:^14}{database[0][1]:^14}{database[0][2]:^16}{database[0][3]:^8}{database[0][4]:^8}{database[0][5]:^10}{database[0][6]:^8}{database[0][7]:>7}{database[0][8]:^12}{database[0][9]:^12}{database[0][10]:^10}{database[0][11]:^10}{database[0][13]:^22}")

    for line in range(0,len(database)):

        if cos in database[line]:
            print(f"{database[line][0]:^14}{database[line][1]:^14}{database[line][2]:^16}{database[line][3]:^8}{database[line][4]:^8}{database[line][5]:^10}{database[line][6]:^8}{database[line][7]:>7}{database[line][8]:>12}{database[line][9]:^12}{database[line][10]:^10}{database[line][11]:^10}{database[line][13]:^22}")
