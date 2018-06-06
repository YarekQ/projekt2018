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
print(odwr("zak"))