##### GCD
number_1 = int(input('Enter the first number: ').strip())
number_2 = int(input('Enter the second number: ').strip())

def simple_gcd(number_1, number_2):
    if number_1 > number_2:
        pass
    else:
        number_1, number_2 = number_2, number_1

    for num in range(1, number_1 + 1):
        if (number_2 % num == 0) & (number_1 % num == 0):
            gcd = num
        else:
            pass
    return gcd

