# devisors of 25 = [1,5,25]

number = int(input('Enter the number: ').strip())

def simple_devisors(number):
    devisros_list = []
    for num in range(1, number + 1):

        if number % num == 0:
            devisros_list.append(num)
        else:
            pass
    return devisros_list

def root_devisors(number):
    divisors = set()
    for num in range(1, int(number**(0.5)) + 1):
        if number % num == 0:
            divisors.add(num)
            divisors.add(number//num)
            print(num, number//num)

    pass

root_devisors(number)
# print(f'All divisors of {number} are {simple_devisors(number)}')