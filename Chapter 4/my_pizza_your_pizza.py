# I am going to write a brand new program because the
# I think there is a typo to the program the book is
# referring to. But, the chances of that are highly unlikely

my_pizza = ['ham', 'cheese', 'pepperoni']
your_pizza = my_pizza[:]

print(my_pizza)
print(your_pizza)

my_pizza.append('anchovies')
your_pizza.append('extra cheese')

print('\nMy favorite pizzas are: ')
print(my_pizza)

print('\nYour pizzas are: ')
print(your_pizza)