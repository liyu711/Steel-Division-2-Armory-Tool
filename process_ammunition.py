import numpy as np
import regex
import json

ammo_data_raw = open("GameData/Generated/Gameplay/Gfx/Ammunition.ndf").read()

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

# DispersionAtMaxRange, DispersionAtMinRange, SupplyCost, TempsDeVisee 这几个是特殊的变量单独拿出来


# test = [i for i in regex.finditer("    PorteeMaximale .*", ammo_data_raw)]
# print(test.__len__())
# print(test)