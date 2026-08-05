class student:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
s1 = student("jerry")
s2 = student("jerry")
s3 = student("tom")
print(s1==s2)
print(s2==s3)