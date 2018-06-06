#otwarciepliku
#fajl=open(ściezka,tryb)
plik=open(r"C:\Users\trusted admin\PycharmProjects\projekt2018\pliktestowy.txt","w",encoding="utf-8")
plik.write("test\ndruga linia\ntrzecia")
plik.write("nastepne linie")
plik.writelines(["5","6","3"])
plik.seek(5)
plik.write("nowy text")

plik.close()
plik=open(r"C:\Users\trusted admin\PycharmProjects\projekt2018\pliktestowy.txt","r",encoding="utf-8")
zmienna=plik.readline()
print(zmienna)
print(plik.readline())
plik.seek(0)
zmienna2=plik.readlines()
print(zmienna2)
#try metody


