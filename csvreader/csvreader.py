import csv
import pickle
from otwieraniebazydanych import otworz
from wyszukajcsv import wyszukajdane

database=otworz(r"c:\Jts\tradesdatabase.bin",'rb')

dane=wyszukajdane()

with open(r"c:\Jts\trades.20180611.csv","r") as file:
    reader = csv.reader(file)
    for line in reader:
        if line not in database:
            database.append(line)



for line in range(0,len(database)):
    print(f"{database[line][0]:14} {database[line][1]:14} {database[line][2]:16} {database[line][3]:8} {database[line][4]:8} {database[line][5]:8} {database[line][6]:8} {database[line][7]:8}\
            {database[line][8]:10} {database[line][9]:8} {database[line][10]:10} {database[line][11]:10} {database[line][12]:10} {database[line][13]:16} {database[line][14]:8}")


#zapisujemy do bazy danych
with open(r"c:\Jts\tradesdatabase.bin",'bw') as file:
    pickle.dump(database,file)