import requests


class Brewery:
    def __init__(self, name: str, brewery_type: str, city: str, country: str):
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.country = country

    def __str__(self) -> str:
        return (f"Browar: {self.name}, typ: {self.brewery_type}, "
                "lokalizacja: {self.city}, {self.country}"
                )


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
