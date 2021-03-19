
# simple way
number = int(input('Enter the number: ').strip())
sum_numbers = [num for num in range(1,number+1)]
print(f'sum of first {number} number is {sum(sum_numbers)}')
