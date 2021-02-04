from .utils import *

class MilitaryPower:
    def __init__(self):
        self.information = 'https://www.globalfirepower.com/countries-listing.asp'
        self.power = {}
        
    def computePower(self):
        page = get_page(self.information)
        countries = page.findAll('a')

        for country in countries:
            if 'country_id' in country['href']:
                if country.find('span', {'class': 'textDkGray'}):
                    power = country.find('span', {'class': 'textDkGray'}).text
                    power = power.replace('\t', '').replace('\n', '').replace('\r', '').split(' ')[1]

                name_container = country.find('div', {'class':'longFormName'})
                if name_container:
                    name = name_container.find('span').text
                    self.power[name] = power
