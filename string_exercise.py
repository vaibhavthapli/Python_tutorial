'''1. Create 3 variables to store street, city and country, now create address variable to
store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line'''

street = "140/25 jakhan"
city = "Dehradun"
country = "India"

address = street + '\n' + city + '\n' + country
print(address)

address1 = f'{street}\n{city}\n{country}'
print(address1)

name = 'Vaibhav Singh Thapli'
home = '140/25 jakhan'
country = 'India'

intro = f'{name} {home} {country}'
print(intro)


'''2. Create a variable to store the string "Earth revolves around the sun"
         1. Print "revolves" using slice operator
         2. Print "sun" using negative index'''

letter = "Earth renolves around the sun"
print(letter[6:14])

print(letter[-3 :])

'''3. Create two variables to store how many fruits and vegetables you eat in a day.
Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
Use python f string for this.'''

fruits = 2
vegetables = 5

print(f"I eat {vegetables} veggies and {fruits} fruits daily")

'''4. I have a string variable called s='maine 200 banana khaye'. This of course is a
wrong statement, the correct statement is 'maine 10 samosa khaye'.
Replace incorrect words in original strong with new ones and print the new string.
Also try to do this in one line.'''

s= "maine 200 banana khaye"
s=s.replace("200","10").replace("banana","samosa")
print(s)