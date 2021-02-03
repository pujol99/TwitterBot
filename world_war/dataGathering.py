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
        self.populations = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
        self.countries = {}
        self.names = set()

    def gatherNames(self):
        page = get_page(self.populations)
        countries = page.find('tbody')

        for country in countries.findAll('tr')[1:]:
            self.names.add(clean(country.find('a')))


    def gatherNeighbours(self):
        page = get_page(self.frontiers)
        countries = page.find('tbody')

        for country in countries.findAll('tr')[3:]:
            name = clean(country.find('td').find('a'))
            if name in self.names:
                self.countries[name] = {
                    "militarypower": 0,
                    "alliance": 0,
                    "neighbours": [clean(a) for a in country.findAll('td')[4].findAll('a') if clean(a) in self.names]
                }

    def cleanNeighbours(self):
        for country in self.countries.keys():
            self.countries[country]['neighbours'] = [country for country in self.countries[country]['neighbours'] if country in self.countries.keys()]

    def toJsonFile(self):
        with open('data/countries.json', 'w') as outfile:
            json.dump(self.countries, outfile, indent=4)
