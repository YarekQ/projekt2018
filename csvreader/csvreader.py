import csv
import pickle
from otwieraniebazydanych import otworz
from wyszukajcsv import wyszukajdane
from dopiszdane import dopisz
from zapis import zapisz
from wydruk import drukuj,filtruj

database=otworz(r"c:\Jts\tradesdatabase.bin",'rb')

dane=wyszukajdane("C:\Jts","n")

dopisz(dane,database)

zapisz(database,r"c:\Jts\tradesdatabase.bin")

drukuj(database)
filtruj(database,"20180615")


