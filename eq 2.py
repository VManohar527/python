class emp:
    def __init__(self, empid, salary):
        self.empid = empid
        self.salary = salary
    def __eq__(self, other):
        return self.empid == other.empid
s1 = emp("jerry",100000)
s2 = emp("jerry",100000)
s3 = emp("tom",200000)
print(s1==s2)
print(s2==s3)