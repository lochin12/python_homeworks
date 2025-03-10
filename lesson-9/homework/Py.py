import csv
import json

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    MAX_BORROW_LIMIT = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {Member.MAX_BORROW_LIMIT} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"'{title}' not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        book = self.find_book(book_title)
        member.borrow_book(book)
        print(f"'{book.title}' has been borrowed by {member.name}")

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        book = self.find_book(book_title)
        member.return_book(book)
        print(f"'{book.title}' has been returned by {member.name}")

library = Library()
library.add_book("The Catcher in the Rye", "J.D. Salinger")
library.add_book("1984", "George Orwell")
library.add_member("Alice")
library.borrow_book("Alice", "1984")

with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Subject", "Grade"])
    writer.writerows([["Alice", "Math", 85], ["Bob", "Science", 78], ["Carol", "Math", 92], ["Dave", "History", 74]])

grades = []
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades.append(row)

subject_grades = {}
for row in grades:
    subject = row["Subject"]
    grade = int(row["Grade"])
    if subject in subject_grades:
        subject_grades[subject].append(grade)
    else:
        subject_grades[subject] = [grade]

with open("average_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, grades in subject_grades.items():
        writer.writerow([subject, sum(grades) / len(grades)])

tasks = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

with open("tasks.json", "r") as file:
    tasks = json.load(file)

completed_tasks = sum(1 for task in tasks if task["completed"])
pending_tasks = len(tasks) - completed_tasks
average_priority = sum(task["priority"] for task in tasks) / len(tasks)

print(f"Total tasks: {len(tasks)}")
print(f"Completed tasks: {completed_tasks}")
print(f"Pending tasks: {pending_tasks}")
print(f"Average priority: {average_priority:.2f}")

with open("tasks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Task", "Completed", "Priority"])
    for task in tasks:
        writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
