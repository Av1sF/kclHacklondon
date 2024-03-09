import requests
import os

def scrape(url):
    data = requests.request("GET", url).text

    buffer = []

    for element in data.split('<a href="')[1:]:
        element = element.split('">')[0]
        if "pdf" in element.lower():
            buffer.append(element)

    i = 0

    for element in buffer:
        name = str(i) + element.rsplit("/")[-1]

        full_path = os.path.join("webscrapeFiles", name)

        print(name)

        with open(full_path, "wb") as f:
            f.write(requests.get(element).content)

        i += 1


file = open('url.txt', 'r')
urls = file.readlines()

for url in urls:
    # adjust url string to exclude '/n' 
    scrape(url[:-2])