class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        srednia = sum(self.marks) / len(self.marks)
        return srednia > 50
    
    def __str__(self):
        return f"Student {self.name}"
    