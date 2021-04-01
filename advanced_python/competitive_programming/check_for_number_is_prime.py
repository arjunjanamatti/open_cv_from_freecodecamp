# prime numbers have two factors 1 and the number itself
# first find all factors and if only 2 factors it is a prime number


number = int(input('Enter the number: '))

def approach_1(number):
    factors_list = set()
    if number == 0 or number == 1:
        return False
    if number == 2 or number == 3:
        return True
    count = 0
    for num in range(1, int((number**0.5)+1)):
        if number % num == 0:
            factors_list.add(num)
            factors_list.add(number//num)
            count += 1
        if count > 2:
            return False

    if len(list(factors_list)) == 2:
        return True
    else:
        return False

def approach_2(number):
    if number == 0 or number == 1:
        return False
    if number == 2 or number == 3:
        return True
    if number%2 == 0 or number%3==0:
        return False
    for i in range(5, int((number**0.5)+1)):
        if number%i == 0 or number%(i+2) == 0:
            return False
    return True


print(approach_2(number))
print(approach_1(number))
