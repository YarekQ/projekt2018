zakupy=["wino","ser","wino czerwone","wino białe","ser do wina bialego","czerwone chablis"]
def niespodzianka(listazak):
    listazak.append("kieliszki")
    listazak.sort()
print(zakupy)
niespodzianka(zakupy)
print(zakupy)

#funkcja z returnem
def odwr(pstring):
    """

    :param pstring: string odwracany
    :return: zwraca odrócony string
    """
    print(pstring)
    return (pstring[::-1])
#funkcje bez returna zwracają "None"

print(odwr("zak"))

#uzycie hintów razem z okreslenien typu wyniku
def polet(podstawa: float, wysok:float) -> float:
    """

    :param podstawa: podstawa
    :param wysok: wysokość
    :return: pole trójkąta
    """
    return 0.5*podstawa*wysok

