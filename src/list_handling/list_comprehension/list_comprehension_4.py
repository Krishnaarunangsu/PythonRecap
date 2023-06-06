#List Comprehension Time Computation
import time

# define function to implement for loop
def for_loop(n):
    """

    :param n:
    :return:
    """
    result=[]
    for i in range(n):
        result.append(i**2)
    return result

# Time Taken by List Comprehension
def list_comprehension(n):
    """

    :param n:
    :return:
    """
    return [i**2 for i in range(n)]

# Driver Code

# Calculate the time taken by the for loop
begin=time.time()
for_loop(10**6)
end=time.time()

# Display time taken by for_loop()
print('Time taken for_loop:', round(end-begin, 2))

# calculate the time taken by list comprehension
begin=time.time()
list_comprehension(10**6)
end=time.time()

# Display time taken by for_loop()
print('Time taken for_loop:', round(end-begin, 2))
