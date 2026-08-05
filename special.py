class car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
    def __str__(self):
        return f"car(model={self.model}, brand={self.brand})"

s = car("m5","bmw")
print(s)