import shutil
import time

#timestamp in GMT used for filename

#start logowania info
startv=time.time()

#liczba sampli
sample=32
plikzsamplami=[]

#czas pomiędzy samplami (w sekundach)
SleepTime=8

StaryCzas,Counter,dif=0,0,0
#plik z ktorego czytane są dane
SourcePlik=r"C:\Users\Enter\AppData\Roaming\MetaQuotes\Terminal\Common\Files\US.500. X-Trade Brokers  status file.csv"
DataPlik=r"d:\python\testfolder\US.500. X-Trade Brokers  status file.csv"
FirstLine=True
dane=[]
InsSyg,Weekly,Daily,Hourly4,Hourly,HalfHourly=[],[],[],[],[],[]
while dif<sample:
    shutil.copy(SourcePlik,DataPlik)
    time.sleep(SleepTime)
    dif=time.time()-startv
    plik=open(DataPlik,"r")
    for i in range(0,83):
        dane.append(plik.readline().strip())
        if FirstLine:
            InsSyg.append(dane[i])
            print(dane[i])
            if i>6:
                FirstLine=False
    plik.close()

Data=InsSyg[0]
Czas=InsSyg[1]
Instrument=InsSyg[2]
Pozycja=InsSyg[3]
Broker=InsSyg[4]
Open=InsSyg[5]
Ask=InsSyg[6]
Bid=InsSyg[7]
print(f" aktualnie: {InsSyg}")

for i in range(0,15):
    Weekly.append(dane[i+8])
    Daily.append(dane[i+23])
    Hourly4.append(dane[i+38])
    Hourly.append(dane[i+53])
    HalfHourly.append(dane[i+68])
MainRSIMatrix=[Weekly,Daily,Hourly4,Hourly,HalfHourly]

#print("weekly",len(Weekly),Weekly)
#print("daily",len(Daily),Daily)
#print("4 hourly",len(Hourly4),Hourly4)
#print("hourly",len(Hourly),Hourly)
#print("half hourly",len(HalfHourly),HalfHourly)

#print(MainRSIMatrix)







print(len(dane))