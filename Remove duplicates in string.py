string = [2, 4, 3, 1, 4, 6, 5, 2, 3, 4, 3, 4, 3, 5, 3, 4]
unique_str =[]
for number in string:
    if number not in unique_str:
        unique_str.append(number)

print(unique_str)