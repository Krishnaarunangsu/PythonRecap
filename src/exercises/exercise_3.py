# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def get_number():
    """
    Get the number
    Args:

    Returns:
        integer: int

    """
    # integer='s'
    input_count=0
    num = input("Enter an integer greater than 0:")
    input_count = +1
    if not num.isdigit():
        while input_count < 2:
            print(f'Input Count:{input_count}')
            num = input("1.Enter an integer greater than 0:")
            input_count = input_count+1
            print(f'2. Here Input Count is:{input_count}')
            if num.isdigit():
                return int(num)
            else:
                num = input("2.Enter an integer greater than 0:")
    else:
        return int(num)



def generate_dictionary(n:int)->dict:
    """
    Generate the dictionary
    Args:
        n:

    Returns:

    """
    Dict={}
    i: int
    for i in range(n):
        x=i+1
        Dict[x]=x*x

    # print(f' THe generated dictionary is:{Dict}')
    return Dict

if __name__=="__main__":
    number=get_number()
    print(f'The entered number is:{number}')
    if number is not None:
        dict_seq=generate_dictionary(number)

    print(dict_seq)
