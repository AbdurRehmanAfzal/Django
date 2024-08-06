class Animals:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def printname(self):
        print(f"The color is {self.color} and the age is {self.age}")

class TIGER(Animals):
    pass

class GOAT(Animals):
    pass

x = TIGER("yellow", 2)
x.printname()

x = GOAT("white", 1)
x.printname()
