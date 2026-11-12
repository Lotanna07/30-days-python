#Day 2: 30 days of python programming 
# Variables in Python
first_name = 'loti'
last_name = 'nwosu'
full_name = "loti nwosu"
country = 'Finland'
city = 'Helsinki'
age = 250
year = 2001
is_married = True
is_true = True
is_light_on = False

#muiltiple variable assignment
x, y, z =1,2,3


print(type(first_name), type(last_name), type(full_name), type(country), type(city), type(age), type(year), type(is_married), type(is_true), type(is_light_on))
print(len(first_name))
print(len(last_name))


num_one = 5
num_two = 4

total = num_one + num_two
print(total)

num_one = 5
num_two = 4

difference = num_one - num_two
print(difference)

num_one = 5
num_two = 4

multiply = num_one * num_two
print(multiply)

division = num_one / num_two
print(division)

modulus = num_one % num_two
print(modulus)

floor_division = num_one // num_two
print(floor_division)

exponential = num_one ** num_two
print(exponential)


import math

# Task 1 & 2: fixed radius of 30
radius = 30

area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

#print("Area:", area_of_circle)              # 2827.4333882308138
#print("Circumference:", circum_of_circle)   # 188.49555921538757

# Task 3: radius from user input
radius_input = float(input("Enter the radius: "))
area_from_input = math.pi * radius_input ** 2

#print("Area from input:", area_from_input)


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

