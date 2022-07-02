# The slice operator [n:m] returns the part of the string from the n’th character to the m’th character,
# including the first but excluding the last. In other words, start with the character at index n and go up to but do
# not include the character at index m. This behavior may seem counter-intuitive but if you recall the range
# function, it did not include its end point either.
# If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the
# second index, the slice goes to the end of the string.
# There is no Index Out Of Range exception for a slice. A slice is forgiving and shifts any offending index to
# something legal.

singers = "Peter, Paul and Mary"
print(singers[0:5])
print(singers[4:5])
print(singers[7:11])
print(singers[17:21])

fruit = 'banana'
print(fruit[:3])
print(fruit[3:])
print(fruit[:])

s = 'python rocks'
print(s[3:8])
print(s[7:11] * 3)
