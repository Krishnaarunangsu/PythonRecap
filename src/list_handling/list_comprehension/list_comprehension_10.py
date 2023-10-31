fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
newlist_1=[]
newlist_1=[x for x in fruits if "a" in x]
print(f'The list comprehension list is:{newlist_1}')