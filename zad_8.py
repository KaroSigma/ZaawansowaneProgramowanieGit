import requests
import argparse


class Brewery:
    def __init__(self, name: str, brewery_type: str, city: str, country: str):
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.country = country

    def __str__(self) -> str:
        return (
            f"Browar: {self.name} ,typ: {self.brewery_type}, "
            f"lokalizacja: {self.city}, {self.country}"
        )


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
        