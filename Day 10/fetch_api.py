import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print("Title:", data['title'])
    print("Body:", data['body'])

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
