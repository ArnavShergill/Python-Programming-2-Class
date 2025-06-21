def dash():
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

print("---- Guided Practice #1 ----\n")

print("--- Dictionary Intro ---\n")

eng2sp = {}

eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

print(eng2sp)

dash()

print("--- Another Way ---\n")

eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
print(eng2sp)

dash()

print("--- Looking Up Value ---\n")

value = eng2sp['two']
print(value)

dash()

print("---- Dictionary Operations ----\n")

print("--- DEL ---\n")

inventory = {'apples' : 430, 'bananas': 312, 'orange': 525, 'pears': 217}
print(inventory)

del inventory['pears']

print(inventory)

dash()

print("--- Mutable ---\n")

inventory = {'apples': 430, 'bananas': 312, 'orange': 525, 'pears': 217}
print(inventory)

inventory['pears'] = 0

print(inventory)

dash()

print("--- adding ---\n")

inventory = {'apples': 430, 'bananas': 312, 'orange': 525, 'pears': 217}
print(inventory)

inventory['bananas'] = inventory['bananas'] + 200
print(", ".join(inventory))

numItems = len(inventory)
print(numItems)

dash()

print("---- Dictionary Methods ----\n")

print("--- Methods ---\n")

inventory = {'apples': 430, "bananas" : 312, "oranges" : 525, "pears": 217}

for akey in inventory.keys():
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)

dash()

print("--- keys ---\n")

inventory = {'apples': 430, "bananas" : 312, "oranges" : 525, "pears": 217}

for k in inventory:
    print("Got key", k)

dash()

print("--- Values/Items ---\n")

inventory = {'apples': 430, "bananas" : 312, "oranges" : 525, "pears": 217}

print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got ", k, "that maps to ", inventory[k])

dash()

print("--- In/Not In ---\n")

inventory = {'apples': 430, "bananas" : 312, "oranges" : 525, "pears": 217}
print("apples" in inventory)
print("cherries" in inventory)

if "bananas" in inventory:
    print(inventory["bananas"])
else:
    print("We have no bananas")

dash()

print("--- Get ---\n")

inventory = {'apples': 430, "bananas" : 312, "oranges" : 525, "pears": 217}
print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))

dash()

print("---- Update Method ----")

print("--- Examples ---\n")

#Existing dictionary
d1 = {'a':1, "b": 2}

#Dictionary to update with
d2 = {'b':3, "c":4}

#Update dictionary
d1.update(d2)

#Output will be {'a': 1, "b":2, "c":3}
print(d1)

dash()

print("--- updating with Key-Value Pairs ---\n")

#existing dictionary
d1 = {'a':1, "b": 2}

#key-value pairs to update with
pairs = [('b', 3), ('c', 4)]

#update dictionary
d1.update(pairs)

#Output will be {'a':1, 'b':3, 'c':4}
print(d1)

dash()

print("--- Updating with Keyword Arguments ---\n")

#existing dictionary
d1 = {'a':1, "b": 2}

#Update Dictionary
d1.update(b=3, c=4)

#Output will be {'a':1, 'b':3, 'c':4}
print(d1)

dash()

print("---- Aliasing ----\n")

opposites = {'up':'down', 'right':'wrong', 'true':'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'

print(opposites['right'])

dash()

print("---- Copying ----\n")

acopy = opposites.copy()
acopy['right'] = 'left'
print(acopy['right'])

dash()
