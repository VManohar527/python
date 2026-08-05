class student:
    def __init__(self, name, marks, roll):
        self.name = name
        self.roll = roll
        self.marks = marks
    def __str__(self):
        return f"Name: {self.name}, roll: {self.roll}, marks:{self.marks}"
    def __repr__(self):
        return f"student('{self.name}', {self.roll}, {self.marks})"
    def __eq__(self, other):
        if isinstance (other, student):
            return self.roll == other.roll
        return False
s1 = student("jerry",100,24)
s2 = student("jerry", 100,24)
s3 = student("tom", 99, 15)
print(s1)
print(repr(s1))
print(s1 == s2)
print(s2 == s3)