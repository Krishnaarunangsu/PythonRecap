def myGen(n):
    yield n
    yield n + 1

for n in myGen(6):
    print(n)