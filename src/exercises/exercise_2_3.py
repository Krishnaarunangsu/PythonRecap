list_1=[]
while len(list_1)<3:
    num = input("Enter an integer:")
    if num.isdigit():
        integer = int(num)
        # print(integer)  # Output: 42
        list_1.append(integer)
    else:
        print(f"{num} is not a valid integer.")

print(list_1)