from auto import Auto

blaszak=Auto("zielony",True,"Audi")
złomek=Auto("rdzawy",True,"Citroen")

auta=[złomek,blaszak]

for auto in auta:
    auto.switchon()

blaszak.mount("turbo")
print(blaszak)

blaszak.napraw()
print(blaszak)
print(złomek)

blaszak.mount("diesel")
złomek.mount("turbo")

print(złomek)

for auto in auta:
    auto.switchon()
print(złomek)

print(blaszak.przebieg)

