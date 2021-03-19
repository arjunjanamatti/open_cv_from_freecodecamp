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
    return list(divisors)

# a = [1,2,3,4,5]
# for i in range(1, len(a)):
#     print(a[i], end=' ')
# or
# print(*a)

# root_devisors(number)
print(f'All divisors of {number} are {root_devisors(number)}')
print(f'All divisors of {number} are {simple_devisors(number)}')