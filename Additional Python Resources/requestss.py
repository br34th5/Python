import requests


#Reminder: Do not name this file requests.py because it won't work
r = requests.get("http://google.com")
status_info = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status"
status = str(r.status_code)

for whatever in status:
    if whatever >= 200 and <= 299:
        print(status, "Successful response")
    else:
        print("IDK")

"""
    if status in status >= 100 and <= 199:
        print("Failed: Informational responses. More info at: ", status_info)
    elif status >= 200 and <= 299:
        print("Successful response")
    elif status >= 300 and <= 399:
        print("Failed: Redirect. More info at: ", status_info)
    elif status >= 400 and <= 499:
        print("Failed: Client error. More info at: ", status_info)
    elif status >= 500 and <= 599:
        print("Failed: Server error. More info at: ", status_info)
    else:
        print("Unexpected error, breaking")
        break
"""
