# string are used to store text data
# ex:- "vaibhav", "thapli"
# Strings are immutable, we can't change values after we create a string.

# String Introduction

from markupsafe import _simple_escaping_wrapper


food = 'samosa'

# Index Operator
food[0]
food[-1]

#String Slicing
food[0:2]
food[:2]
food[-3:-1]
food[-3:]

# len Function
len(food)

# in operator
myfood = "samosa, jalebi"
"samosa" in myfood #True

#replace function
myfood.replce('samosa','biryani') # it can replce samosa with biryani
myfood # output "biryani","jalebi"

#upper and lower function
myfood.upper()
#'BIRYANI, JALEBI'

'ABC'.lower()
# 'abc'


#isdigit and index function
s='145'
s.isdigit() # True

'145a'.isdigit() #False

myfood.index('jalebi') #8


##str function###
states=29
text='total states in india:'
text+states
text+ str(states)

### multiline string using triple quotes ###
dialog='''kitne aadami the?
sardar: do''' 
#'kitne aadami the?\nsardar: do'

### Special characters : newline and tab ###
s='hey\nbro'
print(s)
#hey
#bro

s='hey\tbro'
print(s)
#hey    bro

first ='sachin'
last='tendulkar'
print('The best cricket player:',first + ' '+ last)
#The best cricket player: sachin tendulkar

##Python 3.6 f-string ###
print(f'The best cricket player {first} {last}')
#The best cricket player sachin tendulkar

