from biblioteka.Student import Student
from biblioteka.Employee import Employee

class Order:
    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: list,
        order_date: str,
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = ""
        for book in self.books:
            book_list += (
                f"\n{book.author_name} {book.author_surname} "
                f"({book.number_of_pages} str.)"
            )

        return (
            f"Zamówienie z dnia {self.order_date}\n"
            f"Obsłużony przez: {self.employee}\n"
            f"Wypożyczony przez: {self.student}\n"
            f"Pozycje: {book_list}\n"
        )
