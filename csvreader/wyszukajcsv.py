import os
listaplikowznalezionych=[]
def wyszukajdane(katalog,switch):
    """
    funkcja wyszukuje w podanym katalogu pliki csv zawierające dane
    :return: lista plików
    """
    counter=0
    lista=os.listdir(katalog)
    for plik in lista:
        if "csv" in plik:
            if "trades." in plik:
                listaplikowznalezionych.append(plik)
                counter+=1
    switch=str(switch)
    if switch.upper()=="Y":
        print(f"znalezione pliki: {listaplikowznalezionych}")
    print(f"znaleziono dane w plikach ({counter} plików)\n")
    return listaplikowznalezionych