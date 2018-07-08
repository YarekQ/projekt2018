from zapisdopikla import odczytajzpikla
from os import chdir,getcwd,listdir

listaplikow=[]
CurrentWorkingDirectory=getcwd()

if CurrentWorkingDirectory!="d:\Python":
    chdir("d:\Python")
    print(f"working directory={getcwd()}")

CurrentFileList=listdir("d:\Python")

for item in CurrentFileList:
    if "bin" in item:
        listaplikow.append(item)

for i in range(len(listaplikow)):
    print(i,listaplikow[i])
index=input("input file number:")

nazwapliku=listaplikow[int(index)]

plikzdanymi=odczytajzpikla(nazwapliku)
for item in plikzdanymi:
    print(item)