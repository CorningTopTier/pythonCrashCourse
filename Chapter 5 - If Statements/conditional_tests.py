# Test 1: String equality
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

# Test 2: String inequality
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Test 3: String case sensitivity
print("\nIs car.lower() == 'Subaru'.lower()? I predict True.")
print(car.lower() == 'Subaru'.lower())

# Test 4: Numerical equality
age = 25
print("\nIs age == 25? I predict True.")
print(age == 25)

# Test 5: Numerical inequality
print("\nIs age != 30? I predict True.")
print(age != 30)

# Test 6: Numerical greater than
print("\nIs age > 20? I predict True.")
print(age > 20)

# Test 7: Numerical less than or equal to
print("\nIs age <= 25? I predict True.")
print(age <= 25)

# Test 8: List membership
colors = ['red', 'green', 'blue']
print("\nIs 'green' in colors? I predict True.")
print('green' in colors)

# Test 9: List non-membership
print("\nIs 'yellow' not in colors? I predict True.")
print('yellow' not in colors)

# Test 10: Boolean check
is_raining = False
print("\nIs is_raining == False? I predict True.")
print(is_raining == False)