# # motorcycles = ['honda', 'yamaha', 'suzuski']
# # print(motorcycles)
# #
# # motorcycles.append('ducati')
# # print(motorcycles)
#
# motorcycles = []
#
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
#
# print(motorcycles)
#
# print("-" * 45)
#
# motorcycles = ['honda', 'yamaha', 'suzuki']
#
# motorcycles.insert(0, 'ducati')
# print(motorcycles)
# print("-" * 45)
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
#
# print("-" * 45)
#
# motorcycles = ['honda', 'yamaha', 'suzuki']
#
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")
#
# print("-" * 45)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

### Book is wrong !!!
### No () after too_expensive.

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive} is too expensive for me.")