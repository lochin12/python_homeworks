#q1
def convert_cel_to_far(celsius):
    return celsius * 9 / 5 + 32
def convert_far_to_cel(fahrengeit):
    return (fahrengeit - 32) * 5 / 9
far = float(input("Enter a temperature in degrees F: "))
cel = convert_far_to_cel(far)
print(f"{far} degrees F = {round(cel, 2)} degrees C")
cel = float(input("Enter a temperature in degrees C: "))
far = convert_cel_to_far(cel)
print(f"{cel} degrees C = {round(far, 2)} degrees F")

#q2
def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

initial_amount = float(input("Enter the initial investment amount: "))
annual_rate = float(input("Enter the annual rate of return (as a decimal): "))
years = int(input("Enter the number of years: "))
invest(initial_amount, annual_rate, years)

#q3
num = int(input("Enter positive integer: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(f"{i} is a factor of {num}")

#q4
import statistics
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuition = [uni[2] for uni in universities]
    return students, tuition

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    return statistics.median(numbers)

students, tuition = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuition)

student_mean = mean(students)
student_median = median(students)

tuition_mean = mean(tuition)
tuition_median = median(tuition)

print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}\n")
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("*" * 30)

#5
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))  # True
print(is_prime(15))  # False
print(is_prime(2))   # True

