import unittest
from dataGathering import DataGathering

class DataGatheringTest(unittest.TestCase):

    def test_normalCountry(self):
        self.assertEqual(dg.countries['Andorra']['neighbours'], ['France', 'Spain'])

    def test_UnitedKingdom(self):
        self.assertEqual(
            dg.countries['United Kingdom']['neighbours'], 
            ['Belgium', 'Denmark', 'France', 'Germany', 'Ireland', 'Netherlands', 'Norway'])

    

if __name__ == '__main__':
    dg = DataGathering()
    dg.gatherNames()
    dg.gatherNeighbours()
    dg.cleanNeighbours()
    dg.toJsonFile()
    unittest.main()