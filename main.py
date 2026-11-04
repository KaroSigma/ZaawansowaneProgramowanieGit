from nieruchomosci.House import House
from nieruchomosci.Flat import Flat

from biblioteka.Library import Library
from biblioteka.Book import Book
from biblioteka.Employee import Employee
from biblioteka.Student import Student
from biblioteka.Order import Order

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

bibl1 = Library(
    "Warszawa",
    "Koszykowa 26",
    "00-628",
    "08:00 - 20:00",
    221112233
)
bibl2 = Library(
    "Kraków",
    "Rajska 1",
    "31-124",
    "10:00 - 18:00",
    123456789
)

ksiazka1 = Book(bibl1, "1994", "Andrzej", "Sapkowski", 342)
ksiazka2 = Book(bibl1, "1954", "J.R.R.", "Tolkien", 423)
ksiazka3 = Book(bibl2, "1997", "J.K.", "Rowling", 328)
ksiazka4 = Book(bibl2, "1887", "Bolesław", "Prus", 688)
ksiazka5 = Book(bibl1, "2007", "Dmitry", "Glukhovsky", 544)

pracownik1 = Employee(
    "Jan",
    "Kowalski",
    "2020-05-12",
    "1990-02-14",
    "Warszawa",
    "Złota 44",
    "00-120",
    500111222,
)
pracownik2 = Employee(
    "Anna",
    "Nowak",
    "2018-11-01",
    "1985-08-22",
    "Warszawa",
    "Jasna 10",
    "00-013",
    600333444,
)
pracownik3 = Employee(
    "Piotr",
    "Zieliński",
    "2022-01-15",
    "1995-12-05",
    "Kraków",
    "Floriańska 5",
    "31-019",
    700555666,
)

student1 = Student("Michał", "50, 40, 30, 50")
student2 = Student("Karolina", "40, 40, 40, 50")
student3 = Student("Kamil", "30, 20, 40, 30")

zamowienie1 = Order(
    pracownik1,
    student1,
    [ksiazka1, ksiazka2],
    "2023-10-25"
)
zamowienie2 = Order(
    pracownik3,
    student2,
    [ksiazka3, ksiazka4, ksiazka5],
    "2023-10-26"
)

print(zamowienie1)
print(zamowienie2)

student1 = Student("Paulina", [20, 30, 35])
print(f"Student {student1.name} zdał: {student1.is_passed()}")
student2 = Student("Robert", [70, 90, 85])
print(f"Student {student2.name} zdał: {student2.is_passed()}")
