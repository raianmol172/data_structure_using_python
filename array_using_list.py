# Array using python list
Fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Pomegranate']

#  Accessing an element using its index
F = Fruits[3]
print(F)

# Retrieving through the array
for f in Fruits:
    print(f)

# length of an array
print(len(Fruits))

# modify the existing element
Fruits[4] = 'Cherry'
print(Fruits[4])

# adding new element
Fruits.append('chilly')
Fruits.append('Ginger')
print('After append:')
for x in Fruits:
    print(x)

# to remove an element using its index
Fruits.pop(4)
Fruits.pop(5)
print('After popping element')
for x in Fruits:
    print(x)

# remove the element that has value

Fruits.remove('Apple')
print(Fruits[0])
