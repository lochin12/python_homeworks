import sqlite3

# Task 1
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE Roster (Name TEXT, Species TEXT, Age INTEGER)")
cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])
cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
print(cursor.fetchall())
cursor.execute("DELETE FROM Roster WHERE Age > 100")
cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
cursor.executemany("UPDATE Roster SET Rank = ? WHERE Name = ?", [
    ("Captain", "Benjamin Sisko"),
    ("Lieutenant", "Ezri Dax"),
    ("Major", "Kira Nerys")
])
cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
print(cursor.fetchall())
conn.commit()
conn.close()

# Task 2
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE Books (Title TEXT, Author TEXT, Year_Published INTEGER, Genre TEXT)")
cursor.executemany("INSERT INTO Books VALUES (?, ?, ?, ?)", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])
cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
print(cursor.fetchall())
cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
cursor.executemany("UPDATE Books SET Rating = ? WHERE Title = ?", [
    (4.8, "To Kill a Mockingbird"),
    (4.7, "1984"),
    (4.5, "The Great Gatsby")
])
cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
print(cursor.fetchall())
conn.commit()
conn.close()
