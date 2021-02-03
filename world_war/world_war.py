import requests
from bs4 import BeautifulSoup

url = 'https://mapchart.net/europe.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find('svg'))
