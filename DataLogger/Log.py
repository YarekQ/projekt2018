import shutil
import time
import sys
from GMTFileName import GMTFileName
from zapisdopikla import zapiszdopikla, odczytajzpikla

#start logowania info
startv=time.time()

#lista argumentow programu
listaargv=sys.argv

#plik do ktorego zapisujemy dany
plikzsamplami=[]

#czas pomiędzy samplami (w sekundach)
SleepTime=1
StaryCzas,Counter,dif=0,0,0
#plik z ktorego czytane są dane

SourcePlik=r"C:\Users\Enter\AppData\Roaming\MetaQuotes\Terminal\Common\Files\EURUSD. X-Trade Brokers  status file.csv"
DataPlik=r"d:\Python\Testfolder\EURUSD. X-Trade Brokers  status file.csv"

print("syntax: Log.py [n](integer)= recording time [seconds]; ", end='')
print(listaargv)
print(len(listaargv))
if len(listaargv)==1:
    sample=16
else:
    sample=int(listaargv[1])
print(f"recording not less than {sample} seconds, timestamp={GMTFileName()}")
#SourcePlik=r"c:\Users\trusted admin\AppData\Roaming\MetaQuotes\Terminal\Common\Files\US.500. X-Trade Brokers  status file.csv"
#DataPlik=r"d:\python\US.500. X-Trade Brokers  status file.csv"

while dif<sample:
    shutil.copy(SourcePlik,DataPlik)
    time.sleep(SleepTime)
    dif=time.time()-startv
    plik=open(DataPlik,"r")
    Data=plik.readline().strip()
    Czas=plik.readline().strip()
    if Czas==StaryCzas:
        plik.close()
    else:
        Instrument=plik.readline().strip()
        Pozycja=plik.readline().strip()
        print(f"samp={Counter:4} date={Data:11}time={Czas:9}",end="")
        print(f"inst={Instrument:8} posn={Pozycja:6}",end="")
        Broker=plik.readline().strip()
        print(f"brok={Broker[0:16]:16}",end="")
#unused entry
        plik.readline()
        Ask=plik.readline().strip()
        Bid=plik.readline().strip()
        Spread=float(Ask)-float(Bid)
        #Spread=0
        print(f"ask={Ask:<8}",end="")
        print(f"bid={Bid:<8}",end="")
        print(f"sprd={round(Spread,6):<7}")
        plikzsamplami.append([Data,Czas,Instrument,Pozycja,Broker,Ask,Bid,round(Spread,6)])
        StaryCzas=Czas
        Counter+=1
        plik.close()
print(f"scanning total: {time.time()-startv} second(s)")

nazwapliku=r"d:/python/"+"MTDataFile"+GMTFileName()+".bin"
zapiszdopikla(nazwapliku,plikzsamplami)
