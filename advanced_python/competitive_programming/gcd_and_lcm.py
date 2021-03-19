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

    for num in range(1, number_1 + 1):
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

    for num in range(1, number_1 - 1):
        if (number_2 % num == 0) & (number_1 % num == 0):
            gcd = num
            break
        else:
            pass
    finish = time.perf_counter()
    total_time = round(finish-start, 2)
    return gcd, total_time

gcd_simple, total_time_simple = simple_gcd(number_1, number_2)
gcd_small_improved, total_time_small_improved = simple_gcd(number_1, number_2)

print(f'Greatest common devisor of {number_1} and {number_2} using simple method is {gcd_simple} and time taken: {total_time_simple} seconds')
print(f'Greatest common devisor of {number_1} and {number_2} using simple method is {gcd_small_improved} and time taken: {total_time_small_improved} seconds')
