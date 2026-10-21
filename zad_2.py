class Student:
    def __init__(self, name: str, marks: str):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"Student {self.name}"


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: int):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    
    def __str__(self):
        return f"Biblioteka w {self.city} na ul. {self.street} z kodem pocztowym {self.zip_code}. Otwarte w godzinach {self.open_hours}."
    
class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: int):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik {self.first_name} {self.last_name} zatrudniony {self.hire_date}"

    
class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka autora {self.author_name} {self.author_surname} wydana w {self.publication_date}, posiada {self.number_of_pages} stron, znajduje się w bibliotece: {self.library.city}"  

    
class Order:
    def __init__(self, employee: Employee, student: Student, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = ""
        for book in self.books:
            book_list += f"\n- {book.author_name} {book.author_surname} ({book.number_of_pages} str.)"
    
        return (f"Zamówienie z dnia {self.order_date}\n"
                f"Obsłużony przez: {self.employee}\n"
                f"Wypożyczony przez: {self.student}\n"
                f"Pozycje: {book_list}\n")
    

bibl1 = Library("Warszawa", "Koszykowa 26", "00-628", "08:00 - 20:00", 221112233)
bibl2 = Library("Kraków", "Rajska 1", "31-124", "10:00 - 18:00", 123456789)

ksiazka1 = Book(bibl1, "1994", "Andrzej", "Sapkowski", 342)
ksiazka2 = Book(bibl1, "1954", "J.R.R.", "Tolkien", 423)
ksiazka3 = Book(bibl2, "1997", "J.K.", "Rowling", 328)
ksiazka4 = Book(bibl2, "1887", "Bolesław", "Prus", 688)
ksiazka5 = Book(bibl1, "2007", "Dmitry", "Glukhovsky", 544)

pracownik1 = Employee("Jan", "Kowalski", "2020-05-12", "1990-02-14", "Warszawa", "Złota 44", "00-120", 500111222)
pracownik2 = Employee("Anna", "Nowak", "2018-11-01", "1985-08-22", "Warszawa", "Jasna 10", "00-013", 600333444)
pracownik3 = Employee("Piotr", "Zieliński", "2022-01-15", "1995-12-05", "Kraków", "Floriańska 5", "31-019", 700555666)

student1 = Student("Michał", "50, 40, 30, 50")
student2 = Student("Karolina", "40, 40, 40, 50")
student3 = Student("Kamil", "30, 20, 40, 30")

zamowienie1 = Order(pracownik1, student1, [ksiazka1, ksiazka2], "2023-10-25")
zamowienie2 = Order(pracownik3, student2, [ksiazka3, ksiazka4, ksiazka5], "2023-10-26")

print(zamowienie1)
print(zamowienie2)