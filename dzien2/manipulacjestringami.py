mstring="Zenek Bembenek"

print(mstring.capitalize())
print(mstring.upper())
print(mstring.casefold())
print(mstring.isalnum())

print(mstring.isalpha())

for x in range(0,len(mstring)):
    print(mstring[x:len(mstring)])