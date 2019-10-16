"""
Calculate if given no is palindrome or not
"""


# def palindorme(num):
#     if num == num[::-1]:
#         print("palindrome")
#     else:
#         print("Not palindrome")


def palindrome(num):
    count = 0
    while count<3:
        num = str(num)
        if num == num[::-1]:
            print("Next palindrome no is " + num)
            count +=1

        num = int(num)
        num += 1


number = input("Enter the number:")
palindrome(number)
