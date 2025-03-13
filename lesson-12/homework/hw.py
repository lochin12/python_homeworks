
import sqlite3
import requests
import json
import os
from bs4 import BeautifulSoup
# Task 1: Parse Weather Forecast
def parse_weather():
    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    rows = soup.find("table").find("tbody").find_all("tr")
    weather_data = []
    
    for row in rows:
        cols = row.find_all("td")
        day, temp, condition = cols[0].text, int(cols[1].text[:-2]), cols[2].text
        weather_data.append((day, temp, condition))
    
    # Print weather data
    for entry in weather_data:
        print(entry)
    
    # Find max temp & sunny days
    max_temp = max(weather_data, key=lambda x: x[1])
    sunny_days = [day for day, _, cond in weather_data if cond == "Sunny"]
    avg_temp = sum(temp for _, temp, _ in weather_data) / len(weather_data)
    
    print("Hottest day:", max_temp[0])
    print("Sunny days:", sunny_days)
    print("Average temperature:", avg_temp)

# Task 2: Scrape Job Listings
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            link TEXT,
            UNIQUE(title, company, location)
        )
    """)
    
    jobs = soup.find_all("div", class_="card-content")
    new_jobs = []
    
    for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find_all("p")[1].text.strip()
        link = job.find("a")['href']
        
        cursor.execute("SELECT * FROM jobs WHERE title=? AND company=? AND location=?", (title, company, location))
        existing = cursor.fetchone()
        
        if not existing:
            cursor.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?)", (title, company, location, description, link))
            new_jobs.append((title, company, location))
    
    conn.commit()
    conn.close()
    print(f"New jobs added: {len(new_jobs)}")

# Export jobs to CSV
def export_jobs(filter_by="", value=""):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    query = "SELECT * FROM jobs"
    if filter_by:
        query += f" WHERE {filter_by} = ?"
    cursor.execute(query, (value,)) if filter_by else cursor.execute(query)
    
    jobs = cursor.fetchall()
    conn.close()
    
    with open("jobs.csv", "w", encoding="utf-8") as file:
        file.write("Title,Company,Location,Description,Link\n")
        for job in jobs:
            file.write(",".join(job) + "\n")
    print("Jobs exported to jobs.csv")

# Task 3: Scrape Laptop Data
def scrape_laptops():
    url = "https://www.demoblaze.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    laptops = []
    items = soup.find_all("div", class_="card-block")
    
    for item in items:
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p", class_="card-text").text.strip()
        laptops.append({"name": name, "price": price, "description": description})
    
    with open("laptops.json", "w", encoding="utf-8") as file:
        json.dump(laptops, file, indent=4)
    print("Laptop data saved to laptops.json")

if __name__ == "__main__":
    parse_weather()
    scrape_jobs()
    export_jobs()
    scrape_laptops()
