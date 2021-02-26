

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
operation = input('Enter the opearation between numbers if add, subtract, multiply or devide: ')
if operation == 'add':
    print(f'Addition of {a} and {b} is {calc.add_numbers()}')
elif operation == 'multiply':
    print(f'Multiplication of {a} and {b} is {calc.multiply_numbers()}')
elif operation == 'devide':
    print(f'Division of {a} and {b} is {calc.devide_numbers()}')
elif operation == 'subtract':
    print(f'Subtraction of {a} and {b} is {calc.subtract_numbers()}')
else:
    print(f'Selected {operation} no option available!!!')