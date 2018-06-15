try:
    with open("file.txt") as plik:
        print("moj wierszyk:")
        print(plik.read())
except FileNotFoundError:
    print("nie tutaj tego pliku")
except ValueError:
    print("błąd wartości")
print("koniec programu")