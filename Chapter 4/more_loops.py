my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("")
for food in my_foods:
    print("My foods are " f'{food}'".")
print("")
for his_food in friend_foods:
    print("His food is " f"{his_food}"".")