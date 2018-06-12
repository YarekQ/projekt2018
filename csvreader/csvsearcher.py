import os
listaplikowznalezionych=[]
def wyszukajdane():
    counter=0
    lista=os.listdir(r"C:\Users\Enter\AppData\Roaming\MetaQuotes\Terminal\Common\Files")
    print(lista)
    for plik in lista:
        if "EUR" in plik:
            listaplikowznalezionych.append(plik)
            counter+=1
    print(f"znaleziono dane w plikach ({counter} plików)")
    return listaplikowznalezionych
print(listaplikowznalezionych)