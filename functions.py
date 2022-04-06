# Functions is a block of code that performs a specific task

# Problem: You are given two lists of numbers and you need to find total of each of these list.

list1 = [2100,3400,3500]
list2 = [2000,1500,600]

#with out function
total = 0
for item in list1:
    total = total+ item
print("Total of list1:", total)

total2 = 0
for item2 in list2:
    total2 = total2 + item2
print("Total of list2: ", total2)

#with function

def calculate_total(exp):
    total3= 0
    for item in exp:
        total3 = total3 + item
    return total3
to1 = calculate_total(list1)
to2 = calculate_total(list2)

print("Total of list1: ", to1)
print("total of list2: ",to2)


# Sum of two numbers

def sum(a,b):
    total = a + b
    return total
n = sum(5,6)
print(n)




