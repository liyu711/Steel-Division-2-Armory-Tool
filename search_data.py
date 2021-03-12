import json
import regex

f = open('units.json')
units = json.load(f)

for unit in units:
    print(unit)

print(units["export Descriptor_Unit_Strelki_SOV"])