file_path="numbers.txt"

numbers=[]
with open(file_path, "r") as fp:
    group=[]
    for line in fp:
        if line =="\n":
            numbers.append(group)
            group=[]
        else:
            group.append(int(line.rstrip()))
    # append the last group because if line == "\n" will not be True for
    # the last grou
    numbers.append((group))
print(f'the Numbers are:{numbers}')