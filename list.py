# List is a sequence of memory location where each of the items are stored and these location are accessed by the index.

items = ['bread','pasta','fruits','veggies']
print(items)

# index in list
print(items[0])

#moddify the list
items[0]='chips'
print(items)

#append
items = ['bread','pasta','fruits','veggies']
print(items)
items.append("butter")
print(items)

#append list in a specific location
items = ['bread','pasta','fruits','veggies']
print(items)

items.insert(1,'butter')
print(items)


#join 2 or more lists

food = ['bread','pasta','fruits','veggies']
bathroom = ['shampoo','soap']

new_list = food + bathroom
print(new_list)


