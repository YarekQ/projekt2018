#sekwencja początkowa PNG=‰PNG 4 znaki: 0 137 0x89
#                                       1  80 0x50
#                                       2  78 0x4e
#                                       3  71 0x47

#sekwencja koncowa PNG=END®B`, 7 znaków    69 78 68 174 66 96 130 (7 znaków)
#szesnastkowo:                             45 4E 44  AE 42 60  82 (END®B`)

#sekwencja początkowa jpga= 0xff 0xd8 (2 znaki) = 255 216
#sekwencja końcowa jpga = 0xff 0xd9 (2 znaki)   = 255 217


import math

i=128
#plikzdanymi=open("D:\Python\WHEAT43200.hst","rb").read()
plikzdanymi=open("D:\Python\WIG20.jpg","rb").read()
#plikzdanymi=open("D:\Python\Clipboard02BitfinexWallet.png","rb").read()

print(f"Długość pliku={len(plikzdanymi)}")
#szukanie png
for x in range (0,(len(plikzdanymi)-4)):
    if (plikzdanymi[x])==0x89:
        if (plikzdanymi[x+1])==0x50:
            if (plikzdanymi[x+2])==0x4e:
                if (plikzdanymi[x+3])==0x47:
                    print(f"sekwencja poczatkowa PNG (>‰PNG<, 4 znaki) znaleziona, offset={x}")
    if (plikzdanymi[x]) == 0x45:
        if (plikzdanymi[x + 1]) == 0x4e:
            if (plikzdanymi[x + 2]) == 0x44:
                if (plikzdanymi[x + 3]) == 0xae:
                    if (plikzdanymi[x + 4]) == 0x42:
                        if (plikzdanymi[x + 5]) == 0x60:
                            if (plikzdanymi[x + 6]) == 0x82:
                                print(f"sekwencja końcowa PNG (>END®B`,<, 7 znaków) znaleziona, offset={x}, koniec pliku={x+7}")
#szukanie jpega
for x in range (0,(len(plikzdanymi)-1)):
    if (plikzdanymi[x])==0xff:
        if (plikzdanymi[x+1])==0xd8:
            print(f"sekwencja poczatkowa JPG (>FFD8<, 2 znaki) znaleziona, offset={x}")
    if (plikzdanymi[x]) == 0xff:
        if (plikzdanymi[x + 1]) == 0xd9:
            print(f"sekwencja końcowa JPG (>FFD9<, 2 znaki) znaleziona, offset={x}, koniec pliku={x+2}")
s=40
for j in range (0,1024):
    print(f"{str.rjust(str(int(plikzdanymi[j])),4)}",end="")
    if j%s==0:
        print("\n")
