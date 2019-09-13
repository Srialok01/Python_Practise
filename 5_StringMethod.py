name = 'Alok Srivastava'
# Calculating length of the string - len()
print(len(name))

# Conversion of string into UpperCase
print(name.upper())
print(name)

# Conversion of string into lowercase
print(name.lower())

# Finding the index of a character
print(name.find('o'))
print((name.find('K')))  # When the no is not present in string it will return = -1
print(name.find("sta"))

# Replacing values in string
print(name.replace('Alok', "Rishu"))  # This will print Rishu Srivastava
print(name)  # Original string remains same
print(name.replace("ALOK",
                   "Srres"))  # This will display the initial value of string as 'ALOK' is not present in the original string

# Check if particular value/string is present in the string
print(name)
print('Srivastav' in name)  # This will return true.
