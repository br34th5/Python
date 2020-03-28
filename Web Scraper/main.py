from bs4 import BeautifulSoup
import requests

search = input("Search for:")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

status_code = r.status_code

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

if status_code >= 200 and status_code <= 299:
    print("Success. Status code: ", status_code)
    for item in links:
        item_text = item.find("a").text
        item_href = item.find("a").attrs["href"]
        
        #breaks after: UnicodeEncodeError: 'charmap' codec can't encode character '\u2013' in position 10: character maps to <undefined>
        if item_text and item_href:
            print(item_text)
            print(item_href)
            
            """
            children = item.children
            for child in children:
                print("Child:", child)
            
            children = item.find("h2")
            print("Next sibling is:", children.next_sibling)
            """
else:
    print("No success. ", status_code)