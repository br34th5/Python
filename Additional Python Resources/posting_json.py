import requests
import simplejson as json

url = "https://jsonplaceholder.typicode.com/posts"

#payload is the data that is sent to the URL
payload = {"title": "foo",
           "body": "bar",
           "userID": 1}

#format the payload to json
headers = {"Content-Type": "application/json; charset=UTF-8"}

response = requests.post(url, json=payload, headers=headers)

#print(response.text)
print(response.headers)