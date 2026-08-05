class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"Student(Name={self.name}, marks={self.marks})"
    def __repr__(self):
        return f"('{self.name}' scored{self.marks})"

s = Student("jerry",100)
print(s)
print(repr(s))
