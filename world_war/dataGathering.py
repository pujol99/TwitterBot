from utils import *
import json

class DataGathering:
    """
        "countryname":{
            "militarypower"
            "neighbours"
            "%alliance"
        }   
    """
    def __init__(self):
        self.frontiers = 'https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_land_and_maritime_borders'
        self.countries = {}

    def gather(self):
        page = get_page(self.frontiers)
        countries = page.find('tbody')
        for country in countries.findAll('tr')[3:]:
            name = country.find('a').text
            if name and name not in self.countries.keys():
                self.countries[name] = {
                    "militarypower": 0,
                    "alliance": 0,
                    "neighbours": [a.text for a in country.findAll('td')[4].findAll('a')]
                }
        self.cleanNeighbours()
        
    def cleanNeighbours(self):
        for country, content in self.countries.items():
            self.countries[country] = [neighbour 
                for neighbour in self.countries[country]['neighbours'] 
                if neighbour in self.countries.keys()]

    def toJsonFile(self):
        with open('data/countries.json', 'w') as outfile:
            json.dump(self.countries, outfile, indent=4)

dg = DataGathering()
dg.gather()
dg.toJsonFile()
