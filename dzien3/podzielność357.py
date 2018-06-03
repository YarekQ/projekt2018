liczba=input("podaj liczbę:")
print(f"Zmienna liczba jest {liczba} typu {type(liczba)}5")
#sprawdzenie czy liczba to napewno liczba
if liczba.isdigit():
    liczba=int(liczba)
else:
    print("Źle podałeś")
#zakończenie programu z kodem zakończenia 1
    exit(1)
if liczba%105==0:
    print(f"Liczba {liczba} jest podzielna przez 3 I 5 I 7")
elif liczba%3==0 or liczba%5==0 or liczba%7==0:
    print(f"Liczba {liczba} jest podzielna przez 3 LUB 5 LUB 7")

