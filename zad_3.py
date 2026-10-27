class Property:
    def __init__(self, area: str, rooms: int, price: str, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


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


dom1 = House(
    area="150 m2",
    rooms=5,
    price="1 200 000 PLN",
    address="ul. Kwiatowa 15, Poznań",
    plot=800,
)
mieszkanie1 = Flat(
    area="55 m2",
    rooms=3,
    price="650 000 PLN",
    address="ul. Długa 5/12, Kraków",
    floor="2",
)

print(dom1)
print(mieszkanie1)
