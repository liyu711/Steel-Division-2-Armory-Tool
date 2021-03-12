import pandas as pd
import numpy as np
import json
import re

unit_data_raw = open('../GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf').read()
unit_data_raw = unit_data_raw .replace('(', '{')
unit_data_raw = unit_data_raw .replace(')', '}')
unit_data_raw = unit_data_raw .replace('=', ':')
unit_data_raw = unit_data_raw .replace(" is TEntityDescriptor", " ")
# unit_data_raw = ' '.join(unit_data_raw.split())
temp_output = open('../temp.txt', 'w')
temp_output.write(unit_data_raw)

