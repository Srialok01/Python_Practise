"""
Problem - Program to combine list into a dictionary

"""

list1 = [321,32,3,4,5]
list2 = ['Alok','Amit','Ankit','Rishu','Warid']
y = 0
dict_alok = {}
for x in list1:
    dict_alok[x] = list2[y]
    y += 1
print(dict_alok)
