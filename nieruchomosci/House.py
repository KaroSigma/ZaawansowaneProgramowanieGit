from nieruchomosci.Property import Property


class House(Property):
    def __init__(
        self, area: str, rooms: int, price: str, address: str, plot: int
    ):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"Dom pod adresem: {self.address}, "
            f"Powierzchnia: {self.area}, "
            f"Liczba pokoi: {self.rooms}, "
            f"Rozmiar działki: {self.plot} m2, "
            f"Cena: {self.price}."
        )
