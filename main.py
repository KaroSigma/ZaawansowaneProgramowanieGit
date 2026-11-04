import requests
import argparse

from browary.Brewery import Brewery
from funkcje.zad_1 import powitanie
from funkcje.zad_2 import mnozenie
from funkcje.zad_3 import czy_parzysta
from funkcje.zad_4 import porowywanie_liczb
from funkcje.zad_5 import czy_w_lista
from funkcje.zad_6 import lista_polaczona

print(powitanie("Karolina", "Gluza"))
print(mnozenie(2, 3))

wynik = czy_parzysta(5)
if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

print(porowywanie_liczb(1, 2, 3))
print(czy_w_lista([1, 2, 3], 2))
print(lista_polaczona([1, 2, 3], [2, 3, 4]))

url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

odpowiedz = requests.get(url)
dane_z_api = odpowiedz.json()
lista_browarow = []

for element in dane_z_api:
    nowy_browar = Brewery(
        name=element.get("name"),
        brewery_type=element.get("brewery_type"),
        city=element.get("city"),
        country=element.get("country"),
    )
    lista_browarow.append(nowy_browar)

for browar in lista_browarow:
    print(browar)

parser = argparse.ArgumentParser(
    description="Pobiera informacje o browarach z API."
)

parser.add_argument(
    "--city",
    type=str,
    help="Nazwa miasta do filtrowania browarów (opcjonalne)",
)
args = parser.parse_args()

url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

if args.city:
    url += f"&by_city={args.city}"
    print(f"Szukam browarów w mieście: {args.city}...")
else:
    print("Szukam 20 losowych browarów (nie podano miasta)...")

odpowiedz = requests.get(url)
dane_z_api = odpowiedz.json()

lista_browarow = []

for element in dane_z_api:
    nowy_browar = Brewery(
        name=element.get("name"),
        brewery_type=element.get("brewery_type"),
        city=element.get("city"),
        country=element.get("country"),
    )
    lista_browarow.append(nowy_browar)

if not lista_browarow:
    print("Nie znaleziono żadnych browarów dla podanego miasta.")
else:
    for browar in lista_browarow:
        print(browar)
