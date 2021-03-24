import numpy as np
import regex
import json

ammo_data_raw = open("GameData/Generated/Gameplay/Gfx/Ammunition.ndf").read()
f = open("units_with_weapon.json")
units = json.load(f)

ammo_names_raw = [i for i in regex.finditer("export .*", ammo_data_raw)]
ammo_names = []
for name in ammo_names_raw:
    ammo_names.append(name.group().replace("export ", "").replace(" is TAmmunitionDescriptor", ""))
# print(ammo_names)
print("name count")
print(ammo_names.__len__())

attributes = ["TypeName", "TypeCategoryName", "Caliber", "IsAPCR", "Puissance", "TempsEntreDeuxTirs",
              "TempsEntreDeuxTirs_Min", "TempsEntreDeuxTirs_Max", "TempsEntreDeuxFx", "PorteeMaximale",
              "RadiusSplashPhysicalDamages", "PhysicalDamages",
              "RadiusSplashSuppressDamages", "SuppressDamages", "TirIndirect", "TirReflexe",
              "TempsEntreDeuxSalves", "TempsEntreDeuxSalves_Min", "TempsEntreDeuxSalves_Max",
              "NbTirParSalves", "NbrProjectilesSimultanes", "AffichageMunitionParSalve", "CanHarmInfantry",
              "CanHarmVehicles", "CanHarmHelicopters", "CanHarmAirplanes", "CanHarmGuidedMissiles",
              "IsHarmlessForAllies"]

attribute_dict = {}

for attribute in attributes:
    expression = "    " + attribute + " .*"
    # expression = "^\s*"+attribute
    test = [i for i in regex.finditer(expression, ammo_data_raw)]
    print(attribute)
    print(test.__len__())
    attribute_dict[attribute] = test

max_index = 0
# DispersionAtMaxRange, DispersionAtMinRange, SupplyCost, TempsDeVisee 这几个是特殊的变量单独拿出来
dispersionAtMaxRange = [i for i in regex.finditer("    DispersionAtMaxRange .*", ammo_data_raw)]
# print(dispersionAtMaxRange)
print(dispersionAtMaxRange.__len__())

min_index = 0
dispersionAtMinRange = [i for i in regex.finditer("    DispersionAtMinRange .*", ammo_data_raw)]
# print(dispersionAtMinRange)
print(dispersionAtMinRange.__len__())

supply_index = 0
supplyCost = [i for i in regex.finditer("    SupplyCost .*", ammo_data_raw)]
# print(supplyCost)
print(supplyCost.__len__())

temps_index = 0
tempsDeVisee = [i for i in regex.finditer("    TempsDeVisee .*", ammo_data_raw)]
# print(tempsDeVisee)
print(tempsDeVisee.__len__())

ammunition = {}

for i in range(len(ammo_names)):
    ammo = {
        "name": ammo_names[i]
    }
    for attribute in attributes:
        ammo[attribute] = attribute_dict[attribute][i].group().replace(attribute, "").replace(" ", "").replace("=", "")

    ammunition[ammo_names[i]] = ammo

print(ammunition["Ammo_110mm_Rocket_x6"])

for unit in units:
    units[unit]["ammunition"] = []
    if "ammunition_descriptor" in units[unit]:
        for ammo in units[unit]["ammunition_descriptor"]:
            units[unit]["ammunition"].append(ammunition[ammo])

print(units["203_H17_FIN"]["ammunition"])






# test = [i for i in regex.finditer("    PorteeMaximale .*", ammo_data_raw)]
# print(test.__len__())
# print(test)