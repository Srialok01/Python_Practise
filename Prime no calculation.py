"""
Program to print prime nos in range.
"""

# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# for num in range(num1, num2):
#     if num>1:
#         for i in range(2, num):
#             if num % i ==0:
#                 break
#         else:
#             print(num)

"""
Program to print next prime no
"""
num = int(input("Enter number : "))
for i in range(num+1, 2 * num):
    if num > 1:
        for j in range(2, i):

            if i % j == 0:
                break
        else:

            print(i)
            break




