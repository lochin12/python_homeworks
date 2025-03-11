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
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("You cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise BookNotFoundException(f"{book.title} was not borrowed by you.")
        self.borrowed_books.remove(book)
        book.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book_title):
        book = next((b for b in self.books if b.title == book_title), None)
        if book is None:
            raise BookNotFoundException(f"{book_title} is not available in the library.")
        member.borrow_book(book)

    def return_book(self, member, book_title):
        book = next((b for b in self.books if b.title == book_title), None)
        if book is None:
            raise BookNotFoundException(f"{book_title} is not available in the library.")
        member.return_book(book)

# Task 2 Grades


grades = []
with open('grades.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades.append(row)
subjects = {}
for grade in grades:
    subject = grade['Subject']
    if subject not in subjects:
        subjects[subject] = {'total': 0, 'count': 0}
    subjects[subject]['total'] += int(grade['Grade'])
    subjects[subject]['count'] += 1
averages = []
for subject, data in subjects.items():
    avg_grade = data['total'] / data['count']
    averages.append({'Subject': subject, 'Average Grade': avg_grade})

with open('average_grades.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Subject', 'Average Grade'])
    writer.writeheader()
    writer.writerows(averages)

# Task 3: 


with open('tasks.json', 'r') as file:
    tasks = json.load(file)


for task in tasks:
    print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")


with open('tasks.json', 'w') as file:
    json.dump(tasks, file, indent=4)

def task_stats(tasks):
    total_tasks = len(tasks)
    completed = sum(1 for task in tasks if task['completed'])
    pending = total_tasks - completed
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {avg_priority}")

task_stats(tasks)

def json_to_csv(tasks):
    with open('tasks.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Task', 'Completed', 'Priority'])
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })

json_to_csv(tasks)

library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

member1 = Member("John")
library.add_member(member1)

try:
    library.borrow_book(member1, "The Great Gatsby")
    library.borrow_book(member1, "1984")
    library.borrow_book(member1, "To Kill a Mockingbird")
    library.borrow_book(member1, "Moby Dick")  # This should raise MemberLimitExceededException
except Exception as e:
    print(e)

library.return_book(member1, "1984")
