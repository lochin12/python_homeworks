
num = float(input("Enter a float number: "))
print("Rounded to 2 decimal places:", round(num, 2))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
smallest = num1
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
print("Largest:", largest)
print("Smallest:", smallest)

km = float(input("Enter kilometers: "))
meters = km * 1000
centimeters = km * 100000
print(km, "km =", meters, "meters =", centimeters, "cm")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Integer division:", a // b)
print("Remainder:", a % b)

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

num = int(input("Enter a number: "))
last_digit = num % 10
print("Last digit:", last_digit)

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
