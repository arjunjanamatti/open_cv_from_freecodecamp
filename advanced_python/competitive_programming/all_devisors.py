# devisors of 25 = [1,5,25]

number = int(input('Enter the number: ').strip())
devisros_list = []
for num in range(1,number+1):

    if number%num==0:
        devisros_list.append(num)
    else:
        pass
print(devisros_list)