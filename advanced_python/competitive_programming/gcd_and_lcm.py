import time

##### GCD
number_1 = int(input('Enter the first number: ').strip())
number_2 = int(input('Enter the second number: ').strip())

def simple_gcd(number_1, number_2):
    start = time.perf_counter()
    if number_1 > number_2:
        pass
    else:
        number_1, number_2 = number_2, number_1

    for num in range(1, number_2 + 1):
        if (number_2 % num == 0) & (number_1 % num == 0):
            gcd = num
        else:
            pass
    finish = time.perf_counter()
    total_time = round(finish-start, 2)
    return gcd, total_time

def small_improved_gcd(number_1, number_2):
    start = time.perf_counter()
    if number_1 > number_2:
        pass
    else:
        number_1, number_2 = number_2, number_1

    for num in range(1, number_2 - 1):
        if (number_2 % num == 0) & (number_1 % num == 0):
            gcd = num
            break
        else:
            pass
    finish = time.perf_counter()
    total_time = round(finish-start, 2)
    return gcd, total_time

def euclid_gcd(number_1, number_2):
    # The method introduced by Euclid for computing greatest common divisors is based on the fact that, given two positive integers a and b such that a > b, the common divisors of a and b are the same as the common divisors of a – b and b.
    # So, Euclid's method for computing the greatest common divisor of two positive integers consists of replacing the larger number by the difference of the numbers, and repeating this until the two numbers are equal: that is their greatest common divisor.
    # This method can be very slow if one number is much larger than the other
    if number_1 > number_2:
        pass
    else:
        number_1, number_2 = number_2, number_1
    if number_1 - number_2 == 0:
        return number_1
    return euclid_gcd(number_1-number_2, number_2)

def euclidean_gcd(number_1, number_2):
    # A more efficient method is the Euclidean algorithm, a variant in which the difference of the two numbers a and b is replaced by the remainder of the Euclidean division (also called division with remainder) of a by b.
    # Denoting this remainder as a mod b, the algorithm replaces (a, b) by (b, a mod b) repeatedly until the pair is (d, 0), where d is the greatest common divisor.
    if number_1 > number_2:
        pass
    else:
        number_1, number_2 = number_2, number_1
    if number_2 == 0:
        return number_1
    return euclidean_gcd(number_1 % number_2, number_2)


def lcm(number_1, number_2):
    # lcm(number_1, number_2) = ((number_1 * number_2) / gcd(number_1, number_2))
    product = number_1 * number_2
    gcd = euclidean_gcd(number_1, number_2)
    return product//gcd

print(f'Greatest common devisor of {number_1} and {number_2} is {euclidean_gcd(number_1,number_2)} and Least common multiple is {lcm(number_1,number_2)}')
