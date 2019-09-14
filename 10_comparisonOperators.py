"""
a > b 
a >= b (greater than or equal to) 
a < b 
a <= b 
a == b (equals) 
a != b (not equals)
Problem statement : if temp is greater than 30 then its hot day , if its less than 10 then its a cold day
otherwise neither hot nor cold
"""
temp = input("Enter the temperature : " )
temp = int(temp)
print(type(temp))
if temp >= 30:
    print("Its a hot day ")
elif temp <= 10:
    print("its a cold day")
else:
    print('Its neither hot nor cold day')
"""
problem 2: if name is less than 3 characters long - name must be 3 characters long
otherwise it should not be more than 15 else- name max length can be of 15 characters
otherwise - name looks good
"""
name = input("Enter the name : ")
x = len(name)
if x <= 3:
    print("Name must be 3 characters long ")
elif x >= 15:
    print("Max length of name should be 15 characters")
else:
    print(" Everything looks good !")