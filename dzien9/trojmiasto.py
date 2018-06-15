import requests
from pprint import pprint
from bs4 import BeautifulSoup

#pobranie strony
adres="http://trojmiasto.pl"
odpowiedz=requests.get(adres)

#sprawdzenie czy dostalismy odpowiedz 200 jest ok
print(odpowiedz.status_code)

trojmiasto_zupa=BeautifulSoup(odpowiedz.text,"html.parser")

#wydrukkoduhtml
pprint(odpowiedz.text)

with open("trojmiasto.pl","w") as plik:
    plik.write(odpowiedz.text)
#wyciagamy linki
linki=trojmiasto_zupa.select(".news-list a")
pprint(linki)

#wyciagamy linki
for link in linki:
#text linka
    print(link.getText())
#atrybuty linka
    print(link.attrs)
    print(f"Widomość: {link['title']}")
    print(f"Wiadomość {link('title')}")
    print(f"Wiadomość {str(link)}")

