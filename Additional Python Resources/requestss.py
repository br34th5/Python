import requests


#Reminder: Do not name this file requests.py because it won't work
params = {"q": "pizza"}
r = requests.get("https://www.ecosia.org/search", params=params)
status = r.status_code

print("Status:", status, r.url)

f = open("./page.html", "w+")
f.write(r.text)
