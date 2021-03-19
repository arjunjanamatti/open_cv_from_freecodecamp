
# simple way
number = int(input('Enter the number: ').strip())
sum_numbers = [num for num in range(1,number+1)]


def sum_method_1(number):
    sum_numbers = [num for num in range(1, number + 1)]
    return sum(sum_numbers)

def sum_method_2(number):
    return number * (number+1)//2

print(number/2)
print(number//2)
print(f'sum of first {number} number is {sum_method_1(number)}')
print(f'sum of first {number} number is {sum_method_2(number)}')