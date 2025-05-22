import requests
import csv
import os

url = "https://jsonplaceholder.typicode.com/posts"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()  

    csv_filename = os.path.join(os.path.dirname(__file__), "posts.csv")

    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['userId', 'id', 'title', 'body'])
        writer.writeheader() 
        writer.writerows(data) 

    print(f"Successfully saved {len(data)} posts to {csv_filename}")

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
