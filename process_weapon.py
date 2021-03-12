import re
import regex
import json

weapon_data_raw = open("GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf").read()
f = open('units.json')
units = json.load(f)

expression_dicts = {
    "DefaultSmartHoldFireState": r"DefaultSmartHoldFireState .*",
    "Salvos": r"Salves .*",
    "Ammo Name": r"Ammunition .*",
}


weapon_data_raw = weapon_data_raw.replace('\n', "")
# salvos = [i for i in regex.finditer(r"Salves\W+(\d+\W+)+", weapon_data_raw)]
# print(salvos.__len__())

names = [i for i in regex.finditer(r"export \w+", weapon_data_raw)]
print(names.__len__())

