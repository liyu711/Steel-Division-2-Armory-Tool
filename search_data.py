import json
import regex

f = open('units.json')
units = json.load(f)

print(units["export Descriptor_Unit_Strelki_SOV"])