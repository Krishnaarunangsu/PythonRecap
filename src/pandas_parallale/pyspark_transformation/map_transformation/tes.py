list1 = [2, 3, 4, 5]

print(list(map(lambda x: pow(x, 2), list1)))
print(list(map(lambda x: range(1, x), list1)))


def calc_range(x):
    list_1 = []
    for i in range(x):
        list_1.append(i)

    return list_1


print(calc_range(3))
