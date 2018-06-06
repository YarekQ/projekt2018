liczba=9
lista=["Ala",43,liczba]
print(lista)
#kopiowanie list
lista2=lista[:]
lista3=lista

print(lista2)
print(lista3)
#kopiuje się tylko odniesienie do adresu w pamięci

chemia=["ace","płyn","cola"]
nabial=["mleko","masło","ser"]

zakupyczerwiec=[chemia,nabial]
zakupylipiec=[chemia,nabial]
zakupysierpien=[chemia,nabial]

print(zakupyczerwiec,zakupylipiec,zakupysierpien)

#dodajemy element
zakupylipiec[0].append("żel")
print(zakupyczerwiec,zakupylipiec,zakupysierpien)

#został dodany do "wszystkich" list
#drugi sposób
zakupysierpien=zakupylipiec.copy()
print(zakupylipiec,zakupysierpien)

#można skopiowac wartości tylko element po elemencie