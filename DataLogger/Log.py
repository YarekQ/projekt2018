import shutil
import time
from zapisdopikla import zapiszdopikla, odczytajzpikla

#timestamp in GMT used for filename

GMTLoggingStartTime=time.gmtime()
GMTFileName=str(GMTLoggingStartTime[0])+str(GMTLoggingStartTime[1])+str(GMTLoggingStartTime[2])+str(GMTLoggingStartTime[3])+str(GMTLoggingStartTime[4])+str(GMTLoggingStartTime[5])
print(f"timestamp={GMTFileName}")

#start logowania info
startv=time.time()

#liczba sampli
sample=32
plikzsamplami=[]
#czas pomiędzy samplami (w sekundach)
SleepTime=1
StaryCzas,Counter,dif=0,0,0
#plik z ktorego czytane są dane
SourcePlik=r"c:\Users\trusted admin\AppData\Roaming\MetaQuotes\Terminal\Common\Files\US.500. X-Trade Brokers  status file.csv"
DataPlik=r"d:\python\US.500. X-Trade Brokers  status file.csv"
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
        print(f"sample no.{Counter:4} date={Data:12} time={Czas:10}",end="")
        print(f" instrument={Instrument:10} position={Pozycja:7}",end="")
        Broker=plik.readline().strip()
        print(f" broker={Broker[0:16]:18}",end="")
#unused entry
        plik.readline()
        Ask=plik.readline().strip()
        Bid=plik.readline().strip()
        Spread=float(Ask)-float(Bid)
        #Spread=0
        print(f" ask price={Ask:<8}",end="")
        print(f" bid price={Bid:<8}",end="")
        print(f" spread={round(Spread,6):<8}")
        plikzsamplami.append([Data,Czas,Instrument,Pozycja,Broker,Ask,Bid,round(Spread,6)])
        StaryCzas=Czas
        Counter+=1
        plik.close()
print(f"scanning total: {time.time()-startv} second(s)")
for i in range(0,len(plikzsamplami)):
    print(plikzsamplami[i])
nazwapliku=r"d:/python/"+"MTDataFile"+GMTFileName+".bin"
zapiszdopikla(nazwapliku,plikzsamplami)
