import os
import re
from collections import Counter

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

FILENAME = "employees.txt"

def add_employee():
    with open(FILENAME, "a") as file:
        file.write(input("Enter Employee ID, Name, Position, Salary: ") + "\n")

def view_employees():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            print(file.read())
    else:
        print("No records found")

def search_employee():
    emp_id = input("Enter Employee ID: ")
    with open(FILENAME, "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print(line.strip())
                return
    print("Not found")

def update_employee():
    emp_id = input("Enter Employee ID: ")
    updated = []
    found = False
    with open(FILENAME, "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                found = True
                data = line.strip().split(", ")
                data[1] = input(f"Enter new Name ({data[1]}): ") or data[1]
                data[2] = input(f"Enter new Position ({data[2]}): ") or data[2]
                data[3] = input(f"Enter new Salary ({data[3]}): ") or data[3]
                updated.append(", ".join(data) + "\n")
            else:
                updated.append(line)
    if found:
        with open(FILENAME, "w") as file:
            file.writelines(updated)
    else:
        print("Not found")

def delete_employee():
    emp_id = input("Enter Employee ID: ")
    updated = []
    found = False
    with open(FILENAME, "r") as file:
        for line in file:
            if not line.startswith(emp_id + ","):
                updated.append(line)
            else:
                found = True
    if found:
        with open(FILENAME, "w") as file:
            file.writelines(updated)
    else:
        print("Not found")

def employee_manager():
    while True:
        print("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
        choice = input()
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            break

TEXT_FILE = "sample.txt"
OUTPUT_FILE = "word_count_report.txt"

def read_or_create_file():
    if not os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, "w") as file:
            file.write(input("Enter text: ") + "\n")
    with open(TEXT_FILE, "r") as file:
        return file.read()

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def word_counter():
    text = read_or_create_file()
    word_counts = count_words(text)
    total_words = sum(word_counts.values())

    try:
        top_n = int(input("Top how many words? ") or "5")
    except ValueError:
        top_n = 5

    print(f"\nTotal words: {total_words}")
    with open(OUTPUT_FILE, "w") as file:
        file.write(f"Total Words: {total_words}\n")
        for word, count in word_counts.most_common(top_n):
            print(f"{word} - {count}")
            file.write(f"{word} - {count}\n")

def main():
    while True:
        print("\n1. Test div\n2. Employees\n3. Word Counter\n4. Exit")
        choice = input()
        if choice == "1":
            a, b = map(int, input("Enter two numbers: ").split())
            print(div(a, b))
        elif choice == "2":
            employee_manager()
        elif choice == "3":
            word_counter()
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
