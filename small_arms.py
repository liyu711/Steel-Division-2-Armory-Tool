import regex
import json
import pandas as pd

ammo_data_raw = open("Ammunition.ndf").read()

ammo_names_raw = [i for i in regex.finditer("export .*", ammo_data_raw)]
ammo_names = []
for name in ammo_names_raw:
    ammo_names.append(name.group().replace("export ", "").replace(" is TAmmunitionDescriptor", ""))
# print(ammo_names)
print("name count")
print(ammo_names.__len__())

attributes = ["TypeArme", "TempsEntreDeuxTirs",
              "PorteeMaximale",
              "PhysicalDamages",
              "SuppressDamages",
              "TempsEntreDeuxSalves",
              "NbTirParSalves",
              "PorteeMinimale"]

attribute_dict = {}

for attribute in attributes:
    expression = "    " + attribute + " .*"
    # expression = "^\s*"+attribute
    test = [i for i in regex.finditer(expression, ammo_data_raw)]
    print(attribute)
    print(test.__len__())
    attribute_dict[attribute] = test

ammunition = {}

accuracy_idling = [i for i in regex.finditer("EBaseHitValueModifier/Idling, .*", ammo_data_raw)]
accuracy_moving = [i for i in regex.finditer("EBaseHitValueModifier/Moving, .*", ammo_data_raw)]

for i in range(len(ammo_names)):
    ammo = {
        "name": ammo_names[i]
    }
    for attribute in attributes:
        ammo[attribute] = attribute_dict[attribute][i].group().replace(attribute, "").replace(" ", "").replace("=", "")
    ammo["accuracy_idling"] = accuracy_idling[i].group().replace("EBaseHitValueModifier/Idling,", "").replace(" ", "")
    ammo["accuracy_moving"] = accuracy_moving[i].group().replace("EBaseHitValueModifier/Moving,", "").replace(" ", "")
    ammunition[ammo_names[i]] = ammo

print(ammunition["Ammo_110mm_Rocket_x6"])

def clean_numbers(x):
    x = x.replace("(","").replace("Metre", "").replace(")", "").replace("*", "")
    x = int(x) / 5
    return x

def clean_accuracy(x):
    x = x.replace(")", "").replace(",", "")
    x = float(x) / 100
    return x

ammo_table = pd.DataFrame.from_dict(ammunition).transpose()
print(ammo_table.columns)
print(ammo_table["TypeArme"].unique())
# lmg = ammo_table.loc[ammo_table["TypeArme"] == "'MMG'"]
# lmg["PorteeMaximale"] = lmg["PorteeMaximale"].apply(clean_numbers)
# lmg["PorteeMinimale"] = lmg["PorteeMinimale"].apply(clean_numbers)
# lmg["accuracy_idling"] = lmg["accuracy_idling"].apply(clean_accuracy)
# lmg["accuracy_moving"] = lmg["accuracy_moving"].apply(clean_accuracy)
# lmg = lmg.loc[~lmg.name.str.contains("Air")]
# lmg = lmg.loc[~lmg.name.str.contains("AP")]
# lmg = lmg.loc[~lmg.name.str.contains("HE")]
# lmg = lmg.loc[~lmg.name.str.contains("AA")]
# lmg = lmg.loc[~lmg.name.str.contains("Vehicule")]
# lmg = lmg.loc[~lmg.name.str.contains("vehicule")]
# lmg = lmg.drop(["name", "TypeArme"], axis=1)
# lmg.to_excel("LMG.xlsx")

# rifle = ammo_table.loc[ammo_table["TypeArme"] == "'Rifle'"]
# rifle["PorteeMaximale"] = rifle["PorteeMaximale"].apply(clean_numbers)
# rifle["PorteeMinimale"] = rifle["PorteeMinimale"].apply(clean_numbers)
# rifle["accuracy_idling"] = rifle["accuracy_idling"].apply(clean_accuracy)
# rifle["accuracy_moving"] = rifle["accuracy_moving"].apply(clean_accuracy)
# rifle = rifle.drop(["TypeArme"], axis=1)
# rifle.to_excel("Rifle.xlsx")
# # with open("ammo.json", "w") as out_file:
# #     json.dump(ammunition, out_file)
# rifle_single = rifle.loc[~rifle["name"].str.contains("x")]
# rifle_single = rifle_single.drop(["name"], axis=1)
# rifle_single.to_excel("Rifle_single.xlsx")

smg = ammo_table.loc[ammo_table["TypeArme"] == "'SMG'"]
smg["PorteeMaximale"] = smg["PorteeMaximale"].apply(clean_numbers)
smg["PorteeMinimale"] = smg["PorteeMinimale"].apply(clean_numbers)
smg["accuracy_idling"] = smg["accuracy_idling"].apply(clean_accuracy)
smg["accuracy_moving"] = smg["accuracy_moving"].apply(clean_accuracy)
smg = smg.drop(["TypeArme"], axis=1)
smg.to_excel("Smg.xlsx")
smg_single = smg.loc[~smg["name"].str.contains("x")]
smg_single.to_excel("Smg_single.xlsx")
test = [i for i in regex.finditer("    PorteeMaximale .*", ammo_data_raw)]
print(test.__len__())
# print(test)

# aa_cannon = ammo_table.loc[ammo_table['name'].str.contains("AirAir")]
# print(aa_cannon)
# aa_cannon["PorteeMaximale"] = aa_cannon["PorteeMaximale"].apply(clean_numbers)
# aa_cannon["accuracy_idling"] = aa_cannon["accuracy_idling"].apply(clean_accuracy)
# aa_cannon["accuracy_moving"] = aa_cannon["accuracy_moving"].apply(clean_accuracy)
# aa_cannon.to_excel("aa_cannon.xlsx")
# ag_cannon = ammo_table.loc[ammo_table['name'].str.contains("AirSol")]
# ag_cannon["PorteeMaximale"] = ag_cannon["PorteeMaximale"].apply(clean_numbers)
# ag_cannon["accuracy_idling"] = ag_cannon["accuracy_idling"].apply(clean_accuracy)
# ag_cannon["accuracy_moving"] = ag_cannon["accuracy_moving"].apply(clean_accuracy)
# ag_cannon.to_excel("ag_cannon.xlsx")