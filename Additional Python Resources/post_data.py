import requests

my_data = {"Name": "Einaras", "E-mail": "random@email.com"}
r = requests.post("https://tryphp.w3schools.com/demo/demo_form_post.php", data = my_data)

f = open("post_request.html", "w+")
f.write(r.text)