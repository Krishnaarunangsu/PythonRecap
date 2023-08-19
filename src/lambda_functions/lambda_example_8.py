a = [1, 2, 3 , 4]
b = [lambda: _ for _ in a]
c = [_() for _ in b]
print(a)
print(b)
print(c)