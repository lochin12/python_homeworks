import sqlite3
import pandas as pd

# Part 1: 

conn = sqlite3.connect("chinook.db")
cursor = conn.cursor()
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print(customers_df.head(10))
conn.close()

iris_df = pd.read_json("iris.json")
print(iris_df.shape, iris_df.columns)

titanic_df = pd.read_excel("titanic.xlsx")
print(titanic_df.head())

flights_df = pd.read_parquet("flights.parquet")
print(flights_df.info())

movie_df = pd.read_csv("movie.csv")
print(movie_df.sample(10))

# Part 2: 

iris_df.columns = iris_df.columns.str.lower()
print(iris_df[["sepal_length", "sepal_width"]])

titanic_filtered = titanic_df[titanic_df["Age"] > 30]
print(titanic_filtered)
print(titanic_df["Sex"].value_counts())

print(flights_df[["origin", "dest", "carrier"]])
print(flights_df["dest"].nunique())

movie_filtered = movie_df[movie_df["duration"] > 120]
movie_sorted = movie_filtered.sort_values(by="director_facebook_likes", ascending=False)
print(movie_sorted)

# Part 3: 

print(iris_df.describe())

print(titanic_df["Age"].agg(["min", "max", "sum"]))

print(movie_df.groupby("director_name")["director_facebook_likes"].sum().idxmax())
print(movie_df.nlargest(5, "duration")[["title", "director_name"]])

print(flights_df.isnull().sum())
flights_df.fillna(flights_df.mean(), inplace=True)
