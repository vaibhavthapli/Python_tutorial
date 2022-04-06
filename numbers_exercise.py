# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

long = 92
wide = 48.8
# It's a rectangle and area of rectangle is L*B.
area = long * wide
print("Area of football field: ", round(area,2))


# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

total_packets = 9
per_packet_cost = 1.49
money_paid = 20

total_cost =  total_packets * per_packet_cost

money_return = money_paid - total_cost

print("Money_retun:", money_return)


# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square

length = 5.5
area = length**2 # area of square is lenght power 2
total_cost = area*500

print("total cost for bathroom tiles replacement:",total_cost)


# 4. Print binary representation of number 17.
print("Binary number of 17: ", format(17,'b'))