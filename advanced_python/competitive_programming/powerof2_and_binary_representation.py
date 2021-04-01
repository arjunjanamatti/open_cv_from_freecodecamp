# check if the number is a power of 2

number = int(input('Enter the number: '))

def power_of_2(number):
    if number < 0:
        return False
    x = number
    y = not(number & (number-1))
    return x and y

print(f'{number} is power of 2: {power_of_2(number)}')