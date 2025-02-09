
username = input("Enter username: ")
password = input("Enter password: ")
if username != "" and password != "":
    print("Valid")
else:
    print("Invalid")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == b:
    print("Numbers are equal")
else:
    print("Numbers are different")

num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("Positive and even")
else:
    print("Not both")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a != b and a != c and b != c:
    print("All are different")
else:
    print("Not all different")

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) == len(str2):
    print("Same length")
else:
    print("Different length")

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a + b > 50:
    print("Sum is greater than 50")
else:
    print("Sum is not greater than 50")

num = int(input("Enter a number: "))
if num >= 10 and num <= 20:
    print("Within range")
else:
    print("Out of range")
