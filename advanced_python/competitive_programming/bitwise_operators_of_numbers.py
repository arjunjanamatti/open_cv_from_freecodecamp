# bitwise operator 'and' &
# bitwise operator 'or' |
# bitwise operator 'not' ~
# bitwise operator 'xor' ^
# bitwise operator 'right shift' >>
# bitwise operator 'left shift' <<

# bitwise and operator
number = int(input('Enter the number: '))


# rightshift is divide in power of 2
# 200 >> 3 means 200 // 2**3 which is 200 // 8 = 25

# leftshit is multiply in power of 2
# 200 << 3 means 200 * 2**3 which is 200 * 8 = 1600
def EvenOdd(number):
    if number & 1:
        return 'Odd'
    else:
        return 'Even'


print(f'{number} is {EvenOdd(number)}')