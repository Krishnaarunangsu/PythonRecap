# Functions as Return Values
def parent(num):
    def first_child():
        return "Hi, I'm Elias"

    def second_child():
        return "Call me Ester"

    if num == 1:
        return first_child
    else:
        return second_child
print(parent(1))
print(parent(2))

first=parent(1)
second=parent(2)

print(first())
print(second())