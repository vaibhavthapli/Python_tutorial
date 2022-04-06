''' We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	     32
Pakistan 21'''

# i. Using above create a dictionary of countries and its population

population =  {
    "china": 143,
    "india": 136,
    "USA": 32,
    "Pakistan": 21
}

# ii. Write a program that asks user for three types of inputs.
  #a.  print: if user enter print then it should print all countries with their population in this format.
'''china==>143
    india==>136
    usa==>32
    pakistan==>21'''

 #b. add: if user input add then it should further ask for a country name  to add.

def add():
    country = input("Enter country name to add: ")
    country = country.lower()
    if country in population:
        print("Country is already exist in our dataset.")
        return
    p = input("enter population for {country}:")
    p = float(p)
    population[country]=p #add new key value
    print_all()

 #c. remove: when user inputs remove it should ask for a country to remove.

def remove():
    country = input("enter the country which you want to remove: ")
    country = country.lower()
    if country not in population:
        print("Entered country not present in the dataset.")
        return
    del population[country]
    print_all()

 #d. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.

def query():
    country = input("enter the name of a country.")
    country = country.lower()
    if country not in population:
        print("enter country is not in dataset.")
    print(f"population of {country} is: {population[country]} crore")

def print_all():
    for country , p in population.items():
        print(f"{country}==>{p}")


def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()