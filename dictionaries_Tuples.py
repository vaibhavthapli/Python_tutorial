# a Dictionary is something that allows us to store key , value pairs.

# eg:- Telephone directory

d = {"tom": 9719246465, "vaibhav": 8755918066, "joe" : 7320923203}
print(d['tom'])

# add new number in dictionary
d["sam"] = 8126443499
print(d)

# deleate item from dictionary
del d["sam"]
print(d)

# print all the directory values.

for key in d:
    print("key:", key, "value:", d[key])

#same thing as above but different approach

for k,v in d.items():
    print("key:", key,"value:", v)


#check if a specific person's name is in the dictionary or not .
a = "tom" in d
print(a)

# dleate every thing in a dictionary
d.clear()