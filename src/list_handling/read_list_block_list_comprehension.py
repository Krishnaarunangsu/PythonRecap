file_path="numbers.txt"

with open(file_path, "r") as fp:
    numbers=[list(
        map(
            # str,(line for line in fp.read().rstrip().split("\n\n"))
            int, (line.split())))
        for line in fp.read().rstrip().split("\n\n")
]

print(f'The numbers is:{numbers}')