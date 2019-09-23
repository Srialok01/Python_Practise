"""
Problem : Find the maximum element in list

"""
numbers = [2, 4, 2, 5, 2, 6, 1, 2]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


