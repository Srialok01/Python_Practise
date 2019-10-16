"""
List comprehension is the fastest & elegent way to create list
syntax - [expression for item in list]
"""
"""
# Print a list of elements from 1 to 10
x = [num for num in range(1, 11)]
print(x)

# Print a list of even nos in 0 to 20
even = [num for num in range(0, 21) if num % 2 == 0]
print(even)

# Print a list of nos starting from 2 to 20
nos = [num if num > 2 else num + 1 for num in range(1, 21)]
print(nos)

# Multiply a number to a list
a = [2, 4, 5, 6]
l1 = [x * 3 for x in a]
print(l1)

# Change the number to upper case
a = ['alok', 'satya', 'anil', 'sudhir']
UpperList = [x.upper() for x in a]
print(UpperList)
"""
# Extract number or alphabets in a list
alphanum = "abcs4kmn213"
num = [x for x in alphanum if x.isdigit()]
print(num)

alpha = [x for x in alphanum if x.isalpha()]
print(alpha)

# Extracting first values in the inner list for Nested Lists
nest = [[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']]
f1 = [x[0] for x in nest]
print(f1)

# Printing the square of a list
a = [1, 2, 3, 5, 6]
square = [x * x for x in a]
print(square)

""" 2nd Method"""


def squ(num):
    return num * num


a = [squ(a) for a in range(1, 5)]
print(a)

# Add two list
a = [2, 3, 4, 5, 6]
b = [6, 5, 4, 3, 2]
c =[a[i] + b[i] for i in range(0,len(a))]
print(c)