from audioop import reverse

names = ['jeff', 'mike', 'karl', 'jake', 'makella', 'sara', 'darlene']
print(names)
print(names[0]) # jeff
print(names[0].title()) # Jeff
print(names[1]) # mike
print(names[3]) # jake
print(names[-1]) # darlene
message = f"My name is {names[3].title()}"
print(message) # My name is Jake
names[0] = 'mark'
print(names) #jeff is no more
names.append('harlod') # adds harlod at end
bikes = [] #empty list
bikes.append('honda')
bikes.append('harley')
bikes.append('honda')
print(bikes) # lines 14-16 built list
bikes.insert(0, 'ducati') # puts ducati in front
print(bikes)
del bikes[0] # deletes first index
print(bikes)
fruits = ['apples', 'bananas', 'kiwi']
popped_fruit = fruits.pop()
print(fruits)
print(popped_fruit) # removes last index
fruits.remove('apples') # removed apples
print(fruits)
list = ['apple', 'deli', 'ham', 'item']
list.sort() # alpha order permanent
print(list)
list.sort(reverse=True) # reverse ABC
print(list)
# Temp sort a list in ABC order
order = ['x', 'd','e', 'q']
print(sorted(order))
print(order)
# Reverse order
order.reverse()
print(order)