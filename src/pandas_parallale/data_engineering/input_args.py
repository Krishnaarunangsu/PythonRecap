def split_string(argv):
    # i=0
    # for arg in argv:
    #     i=i+1
    #     print(arg)
    # print(i)
    #Split the string based on space delimiter
    list_strings=argv.split(',')
    print(f'List Length:{len(list_strings)}')
    return list_strings

def join_words(string_list):
    """

    Args:
        string_list:

    Returns:

    """
    space:str=' '
    joined_string=space.join(string_list)
    return joined_string

words=input()
print(words)
string_list=split_string(words)
print(string_list)
space_separated_string=join_words(string_list)
print(space_separated_string)
#myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
