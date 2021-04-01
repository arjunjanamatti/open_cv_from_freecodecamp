# bitwise operator 'and' &
# bitwise operator 'or' |
# bitwise operator 'not' ~
# bitwise operator 'xor' ^
# bitwise operator 'right shift' >>
# bitwise operator 'left shift' <<

# bitwise and operator
number = int(input('Enter the number: '))
power = int(input('Enter the power: '))

# rightshift is divide in power of 2
# 200 >> 3 means 200 // 2**3 which is 200 // 8 = 25

# leftshift is multiply in power of 2
# 200 << 3 means 200 * 2**3 which is 200 * 8 = 1600
def EvenOdd(number):
    if number & 1:
        return 'Odd'
    else:
        return 'Even'

def leftshift(number, power):
    # leftshift is multiply in power of 2
    # 200 << 3 means 200 * 2**3 which is 200 * 8 = 1600
    return number << power

def rightshift(number, power):
    # rightshift is divide in power of 2
    # 200 >> 3 means 200 // 2**3 which is 200 // 8 = 25
    return number >> power

print(f'{number} is {EvenOdd(number)}')
print(f'{number, power} is {leftshift(number, power)}')
print(f'{number, power} is {rightshift(number, power)}')