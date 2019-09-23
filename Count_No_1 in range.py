"""
print nos of 1 in range 1 to 100
"""

# count = 0
# range = list(range(1, 101))
# y = str(range)
# for i in y:
#     if i == '1':
#         count += 1
# print(count)
#


count = 0
for i in range(1, 101):
    if i % 10 == 1 or i // 10 == 1 or i // 10 == 10:
        if i == 11:
            count += 1
            pass
        count += 1
        print(i)
print(count)
