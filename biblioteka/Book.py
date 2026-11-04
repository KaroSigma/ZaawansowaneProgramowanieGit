from biblioteka.Library import Library


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka autora {self.author_name} {self.author_surname} "
            f"wydana w {self.publication_date}, "
            f"posiada {self.number_of_pages} stron, "
            f"znajduje się w bibliotece: {self.library.city}"
        )
    