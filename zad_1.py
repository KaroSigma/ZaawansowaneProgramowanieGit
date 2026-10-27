class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        srednia = sum(self.marks) / len(self.marks)
        return srednia > 50


student1 = Student("Paulina", [20, 30, 35])
print(f"Student {student1.name} zdał: {student1.is_passed()}")
student2 = Student("Robert", [70, 90, 85])
print(f"Student {student2.name} zdał: {student2.is_passed()}")
