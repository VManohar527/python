class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"Student(Name={self.name}, marks={self.marks})"

s = Student("jerry",100)
print(s)