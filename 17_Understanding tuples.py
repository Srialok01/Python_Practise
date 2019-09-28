""" They are like read-only lists. We use them to store a list of items.
But once we define a tuple, we cannot add or remove items or change the existing items"""
numbers = (1, 2, 3, 4, 2, 4, 5, 0)
print(type(numbers))  # This will display type as tuple
print(numbers)
number2 = 2, 3, 1, 4, 2, 4, 3
print(type(number2))  # This too will display tuple

"""Tuple Object doesn't support assignment 
numbers [0] = 1 # This will throw an error 
 """
""" ***************Unpacking**************** """

coordinates = (2, 4, 2)
print(coordinates[0] * coordinates[1] * coordinates[2])  # One way of multiplying values in tuple

""" 2nd way of multiplying tuple"""
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x * y * z)

"""Now unpacking the tuple"""
a,b,c = coordinates
print(a*b*c)
