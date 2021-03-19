
# simple way
number = int(input('Enter the number: ').strip())
sum_numbers = [num for num in range(1,number+1)]
print(sum(sum_numbers))
