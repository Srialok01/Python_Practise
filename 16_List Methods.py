number = [2, 1, 4, 6, 2, 5, 9]
print(number[0])  # Display the first value i.e., 2
print(number[-2])  # Displays the second last digit i.e., 5

""" Appending a value in list """
number.append(8)
print(number)      # This will add 8 in the end of a list

""" Inserting of a value at any index """
number.insert(3, 12)
print(number)      # This will insert 12 at the 4th place of initial string

""" Removing a particular element in"""
number.remove(6)   # This will remove 6 from the list
print(number)

""" Using POP method """
number.pop()
print(number)      # This will remove last item i.e., 8

""" Checking the count """
print(number.count(2))      # This will return the count of 2

"""Check index of any number """
print(number.index(12))

""" To sort the string """
number.sort()
print(number)      # This will sort the value to accending order

""" Reversing a string """
number.reverse()
print(number)       # The will reverse the string

""" Copying a string """
number2 = number.copy()
number.sort()      # Here list is sorted
print(number)      # Here another copy of string is created
print(number2)
