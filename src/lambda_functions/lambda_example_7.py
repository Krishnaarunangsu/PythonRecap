number = [1,2,3,5,4,6,8,9,11,12]
y=int(input(f'Enter the number:'))
multiples_of_4 = list(filter(lambda a: (a%4 == 0) ,range(1,y)))
print(multiples_of_4)