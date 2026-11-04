class Library:
    def __init__(
        self,
        city: str,
        street: str,
        zip_code: str,
        open_hours: str,
        phone: int,
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka w {self.city} na ul. {self.street} "
            f"z kodem pocztowym {self.zip_code}. "
            f"Otwarte w godzinach {self.open_hours}."
        )
