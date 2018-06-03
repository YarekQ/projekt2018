wartość=0
dobieraj=False

while wartość <20:
    karty = input("co dobrałeś? (2...10,J,Q,K,A)")
    for x in range(0,len(karty)):
        karta=karty[x]
        if karta.isdigit()==True:
            if int(karty[x])==0:
               karta=10
            else:
               karta=int(karty[x])
        else:
            if karta.casefold()=="k" or (karta.casefold()=="q" or karta.casefold()=="j"):
               karta=10
            else:
               karta=11
    wartość=wartość+karta
    print("masz na ręku wartość:",wartość)
    if wartość>19:
        if wartość>21:
            print("przegrałeś")
        print("nie dobieraj")
    else:
        print("dobierz")

