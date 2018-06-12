import os
listaplikowznalezionych=[]
def wyszukajdane():
    counter=0
    lista=os.listdir("C:\Jts")
    for plik in lista:
        if "csv" in plik:
            if "trades." in plik:
                listaplikowznalezionych.append(plik)
                counter+=1
    print(f"znaleziono dane w plikach ({counter} plików)")
    return listaplikowznalezionych