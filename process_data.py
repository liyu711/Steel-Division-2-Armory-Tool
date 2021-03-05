import re
import regex
import json

# data_raw = open('temp.txt').read()
# test = re.search(r"// \w+", data_raw)
# data_process1 = re.sub(r"// \w+", "", data_raw)
# data_process2 = re.sub(r"Descriptor_\w+=", " ", data_process1)
# # temp_output = open('temp2.txt', 'w')
# # temp_output.write(data_process2)
# data_process_no_white_space = ' '.join(data_process2.split())
# data_test = re.sub(r'(\w+)',r'"\1"', data_process_no_white_space)
# print(data_test[:200])
# temp_output = open('temp3.txt', 'w')
# temp_output.write(data_test)


# string_test = "TagSet: [Unit1, Unit2, Unit3] abac TagSet:[Unit1, Unit2]"
# # findTest = [i for i in regex.finditer(r"TagSet:(\W+[a-zA-Z]+)+]", string_test)]
# findTest = [i for i in regex.finditer(r"\[(\w+\W+)(\w+[\ ,]+)+\w+\]", string_test)]
# print(findTest)

unitData_raw = open('temp.txt').read()

# expression_dictionary = {
#     "unit_names": r"export \w+",
#     "unit_country": r"MotherCountry .*",
# }
# attributes = {
# }

# names 2212
unit_names = [i for i in re.finditer(r"export \w+", unitData_raw)]
# unit_names = [i for i in re.finditer(r"export Descriptor_Unit_\w+", unitData_raw)]
print(unit_names[0])
print(unit_names.__len__())

#
# # country * 2
# unit_country = [i for i in re.finditer(r"MotherCountry .*", unitData_raw)]
# print(unit_country[0])
# print(unit_country.__len__())
#
# # tagSet * 1
# unit_tags = [i for i in regex.finditer(r"TagSet : \[\W+\w+\W+(\W+\w+\W+)+\w+\W+\]", unitData_raw)]
# print(unit_tags[0])
# print(unit_tags.__len__())
#
# # concealment bonus * 1
# unit_concealment_bonus = [i for i in re.finditer(r"UnitConcealmentBonus .*", unitData_raw)]
# print("# concealment bonus")
# print(unit_concealment_bonus[0])
# print(unit_concealment_bonus.__len__())
#
# auto_cover_index = 0
# # auto cover range 1527
# unit_auto_cover_range = [i for i in re.finditer(r"AutoCoverRange .*", unitData_raw)]
# print("#auto cover range")
# print(unit_auto_cover_range[0])
# print(len(unit_auto_cover_range))
# #
# occupation_index = 0
# # OccupationRadius 1527
# unit_occupation_radius = [i for i in regex.finditer(r"OccupationRadius .*", unitData_raw)]
# print("#occupation radius")
# print(unit_occupation_radius[0])
# print(len(unit_occupation_radius))

# weapon_index = 0
# # weapon descriptor 1997
# unit_weapon = [i for i in regex.finditer(r"\$/GFX/Everything/WeaponDescriptor\w+", unitData_raw)]
# print("# weapon descriptor")
# print(unit_weapon[0])
# print(unit_weapon.__len__())
#
# # actual HP 2212
# unit_damage = [i for i in regex.finditer("MaxDamages .*", unitData_raw)]
# print("# actual HP")
# print(unit_damage[0])
# print(unit_damage.__len__())

# # Displayed HP 2212
# unit_displayed_hp = [i for i in regex.finditer("MaxHPForHUD .*", unitData_raw)]
# print("# displayed HP")
# print(unit_displayed_hp[0])
# print(unit_displayed_hp.__len__())

# # Dangerousness 2212
# unit_dangerousness = [i for i in regex.finditer("Dangerousness .*", unitData_raw)]
# print("# Dangerousness")
# print(unit_dangerousness[0])
# print(unit_dangerousness.__len__())

# # vision range 2212
# unit_vision_range = [i for i in regex.finditer(r"PorteeVision .*", unitData_raw)]
# print("# vision range")
# # print(unit_vision_range[0])
# print(unit_vision_range.__len__())

# # OpticalStrength 2212
# unit_optical_strength = [i for i in regex.finditer(r"OpticalStrength .*", unitData_raw)]
# print("# OpticalStrength")
# print(unit_optical_strength[0])
# print(unit_optical_strength.__len__())

# towable_index = 0
# # IsTowable 1659
# unit_is_towable = [i for i in regex.finditer(r"IsTowable .*", unitData_raw)]
# print("# IsTowable")
# print(unit_is_towable[0])
# print(unit_is_towable.__len__())

# # IsTransporter 2212
# unit_is_transporter = [i for i in regex.finditer(r"IsTransporter .*", unitData_raw)]
# print("# IsTransporter")
# print(unit_is_transporter[0])
# print(unit_is_transporter.__len__())

# # IsPlane 2212
# unit_is_plane = [i for i in regex.finditer(r"IsPlane .*", unitData_raw)]
# print("IsPlane")
# print(unit_is_plane[0])
# print(unit_is_plane.__len__())

# max_speed_index = 0
# # Maxspeed 1659
# unit_max_speed = [i for i in regex.finditer(r"Maxspeed .*", unitData_raw)]
# print("Maxspeed")
# print(unit_max_speed[0])
# print(unit_max_speed.__len__())

speed_combat_index = 0
# Speed combat 1659
unit_speed_combat = [i for i in regex.finditer(r"VitesseCombat .*", unitData_raw)]
# print("Speed Combat")
# print(unit_speed_combat[0])
# print(unit_speed_combat.__len__())

# MaxAcceleration 1659
unit_max_acceleration = [i for i in regex.finditer(r"MaxAcceleration .*", unitData_raw)]
print("MaxAcceleration")
print(unit_max_acceleration[0])
print(unit_max_acceleration.__len__())

# # MaxDeceleration 1659
# unit_max_deceleration = [i for i in regex.finditer(r"MaxDeceleration .*", unitData_raw)]
# print("MaxDeceleration")
# print(unit_max_deceleration[0])
# print(unit_max_deceleration.__len__())
#
# # Half turn time 1659
# unit_half_turn_time = [i for i in regex.finditer(r"TempsDemiTour .*", unitData_raw)]
# print("Half turn time")
# print(unit_half_turn_time[0])
# print(unit_half_turn_time.__len__())
#
# # VehicleSubType 1659
# unit_vehicle_sub_type = [i for i in regex.finditer(r"VehicleSubType .*", unitData_raw)]
# print("VehicleSubType")
# print(unit_vehicle_sub_type[0])
# print(unit_vehicle_sub_type.__len__())
#
# resource_point_index = 0
# # Resource point 2112
# unit_resource_point = [i for i in regex.finditer(r"\{~/Resource_CommandPoints, .*", unitData_raw)]
# print("resource point")
# print(unit_resource_point[0])
# print(unit_resource_point.__len__())
#
# special_attributes_index = 0
# # special attributes 1349
# unit_special_attributes = [i for i in regex.finditer(r"SpecialtiesList : \[\W+\w+\W+(\W+\w+\W+)?\]", unitData_raw)]
# print(unit_special_attributes[0])
# print(unit_special_attributes.__len__())

# # low flying altitude 6636
# plane_low_flying_altitude = [i for i in regex.finditer(r"LowAltitudeFlyingAltitude .*", unitData_raw)]
# print(plane_low_flying_altitude[0])
# print(plane_low_flying_altitude.__len__())

# # NearGroundFlyingAltitude
# plane_near_ground_flying_altitude = [i for i in regex.finditer(r"NearGroundFlyingAltitude .*", unitData_raw)]
# print(plane_near_ground_flying_altitude[0])
# print(plane_near_ground_flying_altitude.__len__())

units = {}
for i in range(unit_names.__len__()):

    # for i in range(attributes["unit_names"].__len__()):
    #     if i < attributes["unit_names"].__len__() - 1:
    #         next_unit_position = attributes["unit_names"][i+1].span()[0]
    #     unit = {
    #         "name": attributes["unit_names"][i].group().replace("export Descriptor_Unit_", "")
    #     }
    if i < (unit_names.__len__() - 1):
        next_unit_position = unit_names[i + 1].span()[0]
    unit = {"name": unit_names[i].group().replace("export Descriptor_Unit_", ""),
            # "country": unit_country[i * 2].group(),
            # "tagSet": ' '.join(unit_tags[i].group()[9:].split())
            # "concealment bonus": unit_concealment_bonus[i].group().replace("UnitConcealmentBonus : ", "")
            # "low flying altitude":
            #     plane_low_flying_altitude[i*3].group().replace("LowAltitudeFlyingAltitude  :", ""),
            # "near ground flying altitude":
            #     plane_near_ground_flying_altitude[i*3].group().replace("NearGroundFlyingAltitude   : ", "")
            # "actual HP": unit_damage[i].group().replace("MaxDamages : ", ""),
            # "displayed HP": unit_displayed_hp[i].group().replace("MaxHPForHUD : ", ""),
            # "dangerousness": unit_dangerousness[i].group().replace("Dangerousness  : ", ""),
            # "vision range": unit_vision_range[i].group().replace("PorteeVision : ", ""),
            # "optical strength": unit_optical_strength[i].group().replace("OpticalStrength : ", ""),
            # "is transporter": unit_is_transporter[i].group().replace("IsTransporter              : ", ""),
            # "is plane": unit_is_plane[i].group().replace("IsPlane                    : ", ""),

            }

    # while (auto_cover_index < len(unit_auto_cover_range)) and \
    #         (unit_auto_cover_range[auto_cover_index].span()[0] < next_unit_position):
    #     unit["auto cover range"] = \
    #         unit_auto_cover_range[auto_cover_index].group().replace("AutoCoverRange             : ", "")
    #     auto_cover_index += 1
    #
    # while (occupation_index < len(unit_occupation_radius)) and \
    #         (unit_occupation_radius[occupation_index].span()[0] < next_unit_position):
    #     unit["occupation radius"] = \
    #         unit_occupation_radius[occupation_index].group().replace("OccupationRadius           : ", "")
    #     occupation_index += 1

    # while (towable_index < len(unit_is_towable)) and \
    #         (unit_is_towable[towable_index].span()[0] < next_unit_position):
    #     unit["towable"] = \
    #         unit_is_towable[towable_index].group().replace("IsTowable                              : ", "")
    #     towable_index += 1

    # while (max_speed_index < len(unit_max_speed)) and \
    #         (unit_max_speed[max_speed_index].span()[0] < next_unit_position):
    #     unit["max speed"] = \
    #         unit_max_speed[max_speed_index].group().replace("IsTowable                              : ", "")
    #     max_speed_index += 1

    while (speed_combat_index < len(unit_speed_combat)) and \
            (unit_speed_combat[speed_combat_index].span()[0] < next_unit_position):
        unit["max speed"] = \
            unit_speed_combat[speed_combat_index].group().replace("VitesseCombat : ", "")
        speed_combat_index += 1

    # while (weapon_index < len(unit_weapon)) and \
    #         (unit_weapon[weapon_index].span()[0] < next_unit_position):
    #     unit["weapons"] = []
    #     unit["weapons"].append(unit_weapon[weapon_index].group())
    #     weapon_index += 1while (weapon_index < len(unit_weapon)) and \
    #         (unit_weapon[weapon_index].span()[0] < next_unit_position):
    #     unit["weapons"] = []
    #     unit["weapons"].append(unit_weapon[weapon_index].group())
    #     weapon_index += 1
    #

    # if i == unit_names.__len__() - 1:
    #     if weapon_index == len(unit_weapon) - 1:
    #         unit["weapons"] = []
    #         unit["weapons"].append(unit_weapon[weapon_index].group())
    #         weapon_index += 1
    # debug
    # print(unit)

    units[unit_names[i].group()] = unit

    # units[attributes["unit_names"][i]] = unit

# print(units[attributes["unit_names"][i]])
print(units[unit_names[0].group()])


# with open("units.json", "w") as out_file:
#     json_obj = json.dump(units, out_file)
