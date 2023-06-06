# Explicit function
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum

# Initializing list
List = [367, 111, 562, 945, 6726, 873]
list_2= [digitSum(i) for i in List if i %2 != 0]
print(list_2)