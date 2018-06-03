liczba=input("podaj liczbę (index miesiąca):")
print(f"Zmienna liczba jest {liczba} typu {type(liczba)}")
#sprawdzenie czy liczba to napewno liczba

if liczba.isdigit():
    liczba = int(liczba)
    if liczba in [1,3,5,7,8,10,12]:
        print("w tym miesiącu jest 31 dni")
    elif liczba in [4,6,9,11]:
        print ("w tym miesiącu jest 30 dni")
    else:
        print("Luty")

