# prime numbers have two factors 1 and the number itself
# first find all factors and if only 2 factors it is a prime number


number = int(input('Enter the number: '))

def approach_1(number):
    factors_list = set()
    for num in range(1, int((number**0.5)+1)):
        if number % num == 0:
            factors_list.add(num)
            factors_list.add(number//num)

    if len(list(factors_list)) == 2:
        return True
    else:
        return False



print(approach_1(number))

