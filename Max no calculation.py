"""
Print the calculate max number in a giver list

"""
numbers = [2, 5, 7, 9, 3, 14]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)
