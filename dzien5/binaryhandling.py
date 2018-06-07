#sekwencja początkowa PNG=‰PNG 4 znaki: 0 137 0x89
#                                       1  80 0x50
#                                       2  78 0x4e
#                                       3  71 0x47

#sekwencja koncowa PNG=END®B`, 7 znaków    69 78 68 174 66 96 130 (7 znaków)
#szesnastkowo:                             45 4E 44  AE 42 60  82 (END®B`)

#sekwencja początkowa jpga= 0xff 0xd8 (2 znaki) = 255 216
#sekwencja końcowa jpga = 0xff 0xd9 (2 znaki)   = 255 217

def paruj(lista1,lista2):
    """
    funkcja wypisuje z dwóch podanych list elementy różniące się o 1 i grupuje je w pary
    podając koniec pliku i początek nastepnego
    :param lista1: lista1
    :param lista2: lista2
    :return: lista par
    """
    wynik=[]
    for i in range(len(lista1)):
        if int(lista1[i]-1) in lista2:
            wynik.append([lista1[i]-1,lista1[i]])
    print(f"znalezione znaczniki: [koniec,poczatek] {wynik}")


def szpng (plikzdanymi):
    """
    funkcja szukająca sygnatury poczatkowej oraz końcowej pliku PNG
    początek pliku - 4 bajty: 89,50,4e,47 (‰PNG)
    koniec pliku - 7 bajtów: 45,4e,44,ae,42,60,82 (END®B`,)
    :param plik: plik przeszukiwany
    :return: True or False (czy plik jest PNG)
             adres poczatkowy oraz końcowy
    """
    plikzdanymi = open(plikzdanymi, "rb").read()
    print(f"Długość pliku={len(plikzdanymi)}")
    foundp = False
    foundk = False
    offsetp=[]
    offsetk=[]
    for x in range (0,(len(plikzdanymi)-6)):
        if (plikzdanymi[x])==0x89:
            if (plikzdanymi[x+1])==0x50:
                if (plikzdanymi[x+2])==0x4e:
                    if (plikzdanymi[x+3])==0x47:
                        #print(f"sekwencja poczatkowa PNG (>‰PNG<, 4 znaki) znaleziona, offset={x}")
                        offsetp.append(x)
                        foundp=True
        if (plikzdanymi[x]) == 0x45:
            if (plikzdanymi[x + 1]) == 0x4e:
                if (plikzdanymi[x + 2]) == 0x44:
                    if (plikzdanymi[x + 3]) == 0xae:
                        if (plikzdanymi[x + 4]) == 0x42:
                            if (plikzdanymi[x + 5]) == 0x60:
                                if (plikzdanymi[x + 6]) == 0x82:
                                    #print(f"sekwencja końcowa PNG (>END®B`,<, 7 znaków) znaleziona, offset={x}, koniec pliku={x+7}")
                                    offsetk.append(x + 6)
                                    foundk=True
    number = min(len(offsetk), len(offsetp))
    found=foundp and foundk
    return (found,number,offsetp,offsetk)

def szjpg (plikzdanymi):
    """
    funkcja szukająca sygnatury poczatkowej oraz końcowej pliku JPG
    początek pliku - 2 bajty: ff,d8
    koniec pliku - 2 bajty: ff,d9
    :param plikzdanymi:
    :return: True or False (czy plik jest PNG)
             adres poczatkowy oraz końcowy
    """
    plikzdanymi = open(plikzdanymi, "rb").read()
    #print(f"Długość pliku={len(plikzdanymi)}")
    foundp = False
    foundk = False
    offsetp = []
    offsetk = []
    for x in range (0,(len(plikzdanymi)-1)):
        if (plikzdanymi[x])==0xff:
            if (plikzdanymi[x+1])==0xd8:
                #print(f"sekwencja poczatkowa JPG (>FFD8<, 2 znaki) znaleziona, offset={x}")
                offsetp.append(x)
                foundp = True
        if (plikzdanymi[x]) == 0xff:
            if (plikzdanymi[x + 1]) == 0xd9:
                #print(f"sekwencja końcowa JPG (>FFD9<, 2 znaki) znaleziona, offset={x}, koniec pliku={x+2}")
                offsetk.append(x+1)
                foundk = True
    number=min(len(offsetk),len(offsetp))
    found = foundp and foundk
    return (found, number, offsetp, offsetk)

def zapiszpng(plikzdanymi,ap,ak):
    """
    funkcja zapisuje zakres bajtów od ap do ak do pliku z rozszerzeniem PNG
    :param plikzdanymi: plik z którego czytamy dane
    :param ap: adres początkowy
    :param ak: adres końcowy
    :return:
    """
    plikzdanymi = open(plikzdanymi, "rb").read()
    plikwynik= open(r"D:\Python\plik.png","wb")
    plikwynik.write(plikzdanymi[ap:ak])
    plikwynik.close()

def zapiszjpg(plikzdanymi,ap,ak):
    """
    funkcja zapisuje zakres bajtów od ap do ak do pliku z rozszerzeniem JPG
    :param plikzdanymi: plik z którego czytamy dane
    :param ap: adres początkowy
    :param ak: adres końcowy
    :return:
    """
    plikzdanymi = open(plikzdanymi, "rb").read()
    jpgfilename="D:\Python\plik"+str(ap)+str(ak)+".jpg"
    plikwynik= open(jpgfilename,"wb")
    plikwynik.write(plikzdanymi[ap:ak])
    plikwynik.close()

#szukanie plików PNG
print(szpng(r"D:\Python\treasure_inside"))
#szukanie JPG
print(szjpg(r"D:\Python\treasure_inside"))

#parowanie początków/końców plików
paruj([219516, 267818, 280124, 334555, 685623, 972966, 974090, 982827, 1177591],[26445, 33537, 138658, 179340, 192471, 197330, 211869, 253791, 278682, 303676, 685622, 972965, 981332, 990069, 1177590, 1312003])

#zapis plików
zapiszpng(r"D:\Python\treasure_inside",0,334554)
zapiszjpg(r"D:\Python\treasure_inside",334555,685622)
zapiszjpg(r"D:\Python\treasure_inside",685623,972965)
zapiszjpg(r"D:\Python\treasure_inside",972966,1177590)
zapiszjpg(r"D:\Python\treasure_inside",1177591,1312003)