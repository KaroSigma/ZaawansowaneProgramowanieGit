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
