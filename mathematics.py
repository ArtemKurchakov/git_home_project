class Mathematics():

    def __init__(self):
        self.mathematics = [5, 6, 7, 10]

    def multiplication(self):
        for a in self.mathematics:
            print(a * 3)

    def subtraction(self):
        for a in self.mathematics:
            print(a - 5)

    def division(self, a, b):
        if b == 0:
            print("Cannot be divided by zero! Enter a different number instead of zero!!!")
        else:
            return a / b