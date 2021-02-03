from bs4 import BeautifulSoup
import requests

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup