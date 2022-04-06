# 1.Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see
# Ans: We got syntax error because breake is a predefined item in python.

# 2. Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables.

from zmq import THREAD_SCHED_POLICY


birth_year = 1997
current_year = 2022

Age = current_year - birth_year
print(Age)

# 3.Store your first, middle and last name in three different variables and then print your full name using these variables.

first = "Vaibhav"
Second = "Singh"
Last = "Thapli"

print("My Full name is: ",first +" "+ Second +" "+ Last)