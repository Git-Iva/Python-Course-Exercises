# Scrape a paragraph from a given webpage

from bs4 import BeautifulSoup
import requests


url = "https://en.wikipedia.org/wiki/Mathematics"
response = requests.get(url)

if response is not None:
    html = BeautifulSoup(response.content, "html.parser")
    title = html.select("#firstHeading")[0].text
    paragraphs = html.select("p")
    for para in paragraphs:
        print(para.text)

# Grab selected text only
intro = "\n".join(para.text for para in paragraphs[0:5])

# Write intro into an output file
with open("intro.txt", "w") as f:
    f.write(intro)