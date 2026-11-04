from nieruchomosci.Property import Property


class Flat(Property):
    def __init__(
        self, area: str, rooms: int, price: str, address: str, floor: str
    ):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Mieszkanie pod adresem: {self.address}, "
            f"Powierzchnia: {self.area}, "
            f"Liczba pokoi: {self.rooms}, "
            f"Piętro: {self.floor}, "
            f"Cena: {self.price}."
        )
