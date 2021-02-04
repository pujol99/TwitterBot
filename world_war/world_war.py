from src.dataGathering import DataGathering
from src.militarPower import MilitaryPower
from src.utils import *
import random

data = fromJsonFile()

i = 0
total = 0
for country in data:
    if data[country]['militarypower']:
        i += 1
    total += 1

print(i/total)