


number = int(input('Enter the number: '))

def check_prime(number):
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

def prime_upto_N(number):
    num_list = []
    for num in range(1, number):
        if check_prime(num):
            num_list.append(num)
    return num_list

print(f'Prime Numbers till {number} is {prime_upto_N(number)}')