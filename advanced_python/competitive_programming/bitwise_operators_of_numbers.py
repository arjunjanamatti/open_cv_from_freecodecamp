# bitwise operator 'and' &
# bitwise operator 'or' |
# bitwise operator 'not' ~
# bitwise operator 'xor' ^
# bitwise operator 'right shift' >>
# bitwise operator 'left shift' <<

# bitwise and operator
number = int(input('Enter the number: '))

def EvenOdd(number):
    if number & 1:
        return 'Odd'
    else:
        return 'Even'


print(f'{number} is {EvenOdd(number)}')