import re
import regex
import json

weapon_data_raw = open("GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf").read()
f = open('units.json')
units = json.load(f)

weapons_data = {}

weapon_data_raw = weapon_data_raw.replace('\n', "")

# 2087
names = [i for i in regex.finditer(r"export \w+", weapon_data_raw)]
print(names.__len__())

# 2087
salvos = [i for i in regex.finditer(r"Salves\W+(\d+\W+)+", weapon_data_raw)]
print(salvos.__len__())

# 7015
ammunition = [i for i in regex.finditer(r"~/Ammo_\w+", weapon_data_raw)]
print(ammunition.__len__())

for name in names:
    weapon_descriptor = {
        "name": name
    }
# for unit in units:
#     if "weapons" in units[unit]:
#         print(units[unit]["weapons"])
