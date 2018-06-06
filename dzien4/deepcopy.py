import copy

chemia=["ace","płyn","cola"]
nabial=["mleko","masło","ser"]
#kopiowanie płytkie (adresy)

zakupyczerwiec=[chemia,nabial]
zakupylipiec=copy.deepcopy(zakupyczerwiec)
zakupysierpien=copy.deepcopy(zakupyczerwiec)

zakupylipiec[0].append("zel")

print(zakupyczerwiec)
print(zakupylipiec)
print(zakupysierpien)

