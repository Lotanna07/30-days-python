age = 20
height = 5.9
complex_num = 3 + 4j



print(age)
print(height)
print(complex_num)

#4
base = 20
height = 10
area = 0.5 * base * height
print("Area of triangle:", area)

#5
a = 5
b = 4
c = 3
perimeter = a + b + c
print("Perimeter of triangle:", perimeter)

#6
length = 10
width = 5
area = length * width
perimeter = 2 * (length + width)
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)


#7
pi = 3.14
r = 5
area = pi * r * r
circumference = 2 * pi * r
print("Area of circle:", area)
print("Circumference of circle:", circumference)


#8
# Line: y = 2x - 2
# Compare with y = mx + b  ->  m = 2, b = -2

m = 2
b = -2

slope = m
y_intercept = b
x_intercept = -b / m      # solve 0 = mx + b  ->  x = -b/m

print("Slope:", slope)              # Slope: 2
print("y-intercept:", y_intercept)  # y-intercept: -2
print("x-intercept:", x_intercept)  # x-intercept: 1.0


#9
import math

# The two points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope:  m = (y2 - y1) / (x2 - x1)
slope = (y2 - y1) / (x2 - x1)

# Euclidean distance:  d = sqrt((x2-x1)**2 + (y2-y1)**2)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Slope:", slope)         # Slope: 2.0
print("Distance:", distance)   # Distance: 8.94427190999916


#10
# Task 8: slope of y = 2x - 2
slope_task8 = 2

# Task 9: slope between (2,2) and (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_task9 = (y2 - y1) / (x2 - x1)   # 8/4 = 2.0

# Compare them
print(slope_task8 == slope_task9)   # True  -> they are equal
print(slope_task8 > slope_task9)    # False
print(slope_task8 < slope_task9)    # False



#11
# Calculate y = x^2 + 6x + 9 for different x values
for x in range(-6, 3):
    y = x**2 + 6*x + 9
    print(f"x = {x:3}  ->  y = {y}")

# Find where y == 0
for x in range(-10, 10):
    y = x**2 + 6*x + 9
    if y == 0:
        print("\ny is 0 when x =", x)


#12
python_length = len("python")
dragon_length = len("dragon")

print(python_length)   # 6
print(dragon_length)   # 6

# Falsy comparison (evaluates to False)
is_python_longer = python_length > dragon_length
print(is_python_longer)   # False



#13
print('on' in 'python' and 'on' in 'dragon')


#14
sentence = "I hope this course is not full of jargon."

print('jargon' in sentence)   # True

#15
print('on' not in 'dragon' and 'on' not in 'python')  # False


#16
x = len("python")
print(x)

as_float = float(x)
as_string = str(as_float) 


#17
number = 8

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")




#18
 print(7 // 3 == int(2.7))   # True

#19
print(type('10') == type(10))   # False

#20
print(int('9.8') == 10)   # False

#21
hours = input("Enter hours: ")
rate = input("Enter rate per hour: ")

hours = float(hours)
rate = float(rate)

pay = hours * rate

print("Your weekly earning is", pay)

#22
year = int(input("Enter a year: "))

seconds = year * 365 * 24 * 60 * 60

print("You have lived for", seconds, "seconds.")


#23
for n in range(1, 6):
    print(n, n**0, n**1, n**2, n**3)





