from bs4 import BeautifulSoup
import requests

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def valid_country(country):
    """
    - Has more than half million population
    """
    country_population = int(country.findAll('td')[1].text.replace(',', ''))
    return country_population > 500000

def find_neighbours(country, valid_countries):
    neighbours = []

    for tag in country.findAll('td')[4].findChildren(recursive=False):
        if tag.name == 'i':
            break
        if tag.name == 'a' and tag.text and tag.text in valid_countries:
            neighbours.append(tag.text)

    return neighbours