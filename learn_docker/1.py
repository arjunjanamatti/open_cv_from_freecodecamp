

class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add_numbers(self):
        return self.a + self.b

    def subtract_numbers(self):
        return self.a - self.b

    def multiply_numbers(self):
        return self.a * self.b

    def devide_numbers(self):
        return self.a / self.b

    pass

a = int(input('Enter the first variable: '))
b = int(input('Enter the second variable: '))
calc = calculator(a,b)
print(f'Addition of {a} and {b} is {calc.add_numbers()}')
print(f'Multiplication of {a} and {b} is {calc.multiply_numbers()}')
print(f'Division of {a} and {b} is {calc.devide_numbers()}')
print(f'Subtraction of {a} and {b} is {calc.subtract_numbers()}')