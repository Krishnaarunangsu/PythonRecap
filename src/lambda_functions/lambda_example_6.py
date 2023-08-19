# Lambda with Map
# number = [5,10,15,20,25,30,35,40,45,50]
y=int(input(f'Enter the number:'))
newnumber = list(map(lambda c: c*5 ,range(1,y)))
print(newnumber)