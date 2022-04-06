'''Using following list of cities per country
india = ["mumbai","banglore","chennai","delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka","khulna","rangpur"]'''

''' 1. Write a program that asks user to enter a city name and it should tell which country the city belongs to.'''

india = ["mumbai","banglore","chennai","delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka","khulna","rangpur"]

'''city = input("Enter a city name: ")

if city in india:
    print("India")
elif city in pakistan:
    print("Pakistan")
elif city in bangladesh:
    print("Bangladesh")
else:
    print("I don't know")'''

'''2. Write a program that asks user to enter two cities and it tells you if
they both are in same country or not.
For example: if I enter mumbai and chennai, it will print "Both cities are in indai"
but if I enter mumbai and dhaka it should print "They don't belong to same country'''

city1 = input("Enter city 1: ")
city2 = input("Enter city 2: ")

if city1 and city2 in india:
    print("Both cities in india.")
elif city1 and city2 in pakistan:
    print("Both cities in pakistan")
elif city1 and city2 in bangladesh:
    print("Both cities in bangladesh")
else:
    print("They don't belong to same country")


'''Write a python program that can tell you if your sugar is normal or not.
Normal fasting level suger range is 80 to 100.

i. Ask user to enter his fasting sugar level
ii. If it is between 80 to 100 range then print that sugar is low
iii. if it is above 100 then print that it is high otherwise print that it is normal.'''

sugar = float(input("Please enter your fasting sugar level: "))
if sugar<80:
    print("Your suagr is low.")
elif sugar>100:
    print("Your suagr is high")
else:
    print("Your sugar is normal.")