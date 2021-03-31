


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
    # check if every number from 1 to number is a prime
    num_list = []
    for num in range(1, number):
        if check_prime(num):
            num_list.append(num)
    return num_list

def gen_primes(number):
    primes  = [True]*(number+1)
    primes[0] = False
    primes[1] = False
    for p in range(2, int((number**0.5)+1)):
        if primes[p] == True:
            for i in range(p*p, number+1, p):
                primes[i] = False

    prime_list = []
    for i in range(0,len(primes)):
        if primes[i] == True:
            prime_list.append(i)
    return prime_list
print(f'Prime Numbers till {number} is {prime_upto_N(number)}')
print(f'Prime Numbers till {number} is {gen_primes(number)}')