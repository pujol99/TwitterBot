import unittest
from dataGathering import DataGathering

class DataGatheringTest(unittest.TestCase):

    def test_BigCountry(self):
        self.assertEqual(
            dg.countries['United Kingdom']['neighbours'], 
            ['Belgium', 'Denmark', 'France', 'Germany', 'Ireland', 'Netherlands', 'Norway'])
        self.assertEqual(
            dg.countries['Afghanistan']['neighbours'], 
            ['China', 'Iran', 'Pakistan', 'Tajikistan', 'Turkmenistan', 'Uzbekistan'])
        self.assertEqual(
            dg.countries['Venezuela']['neighbours'], 
            ['Brazil', 'Colombia', 'Dominican Republic', 'France', 'Guyana', 'Netherlands', 'Trinidad and Tobago'])
        self.assertEqual(
            dg.countries['Spain']['neighbours'], 
            ['Algeria', 'France', 'Italy', 'Morocco', 'Portugal'])
        self.assertEqual(
            dg.countries['Russia']['neighbours'], 
            ['Azerbaijan', 'Belarus', 'China', 'Estonia', 'Finland', 'Georgia', 'Japan', 'Kazakhstan', 'North Korea', 
            'Latvia', 'Lithuania', 'Mongolia', 'Norway', 'Poland', 'Romania', 'Sweden', 'Turkey', 'Ukraine', 'United States'])

    def test_SmallCountry(self):
        with self.assertRaises(KeyError):
            dg.countries['Samoa']
        with self.assertRaises(KeyError):
            dg.countries['Barbados']
        with self.assertRaises(KeyError):
            dg.countries['Iceland']

    def test_IslandCountry(self):
        with self.assertRaises(KeyError):
            dg.countries['Sint Maarten']
        with self.assertRaises(KeyError):
            dg.countries['Saint Martin']
        with self.assertRaises(KeyError):
            dg.countries['Queen Maud Land']
                

if __name__ == '__main__':
    dg = DataGathering()
    dg.gatherNames()
    dg.gatherNeighbours()
    dg.toJsonFile()
    unittest.main()