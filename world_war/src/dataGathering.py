from .utils import *

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

        # Read first 180 countries that have more than half million population
        for country in countries.findAll('tr')[1:180]:
            if valid_country(country):
                self.names.add(country.find('a').text)


    def gatherNeighbours(self):
        page = get_page(self.frontiers)
        countries = page.find('tbody')

        for country in countries.findAll('tr')[3:]:
            name = country.find('td').find('a').text
            if name in self.names - set(self.countries):
                self.countries[name] = {
                    "militarypower": 0,
                    "alliance": 0,
                    # Get neighbours column and check that they are valid countries
                    "neighbours": find_neighbours(country, self.names)}
