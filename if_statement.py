'''Write a program that ask user to enter a number.
Program should then tell if number is odd or even.'''

num = int(input("Enter a number: "))

if num%2==0:
    print("number is even")
else:
    print("number is odd")

print(type(num)) # it only use in python # for numpy we use (dtype)



'''Write a program that asks user to enter dish name and it should print which cuisine is that dish.'''

indian = ["samosa","daal",'naan']
chinese = ["egg role","pot sticker","fried rice"]
italian = ["pizza","pasta","risotto"]


dish = input("Enter the dish name: ")

if dish in indian:
    print("indian")

elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("Based on little knowledge I have I don't know which cusine is",dish)
