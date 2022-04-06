'''Store monthly expenses in a list and find out total expenses for all months.'''
exp = [2340,2500,2100,3100,2980]
total = 0
for item in exp:
    total = total + item
print(total) 

'''Print 1 to 12 using range()'''
for i in range(1,13):
    print(i)

'''In our monthly expense example, print month number and expense and then in the
end print total expense'''

exp = [2340,2500,2100,3100,2980]
total = 0
for i in range(len(exp)):
    print("Month: ",(i+1), "Expense: ",exp[i])
    total = total + exp[i]
    print("total", total)

'''Search for lost car key in home and when found stop serching '''

key_location = "chair"
locations = ["garage", "living room","chair","closet"]

for i in locations:
    if i==key_location:
        print("Key is found in ",i)
        break
    else:
        print("keys is not found in ", i)

'''Print square of numbers between 1 to 5 EXCEPT even number'''
'''we use continue to skip'''
for i in range(1,6):
    if i%2== 0 :
        continue 
    print(i*i)


'''While Statement'''
'''Print numbers 1 to 5'''

i =1
while i<=5:
    print(i)
    i = i+1