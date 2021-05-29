# import pandas as pd
#
#
# raw_df = pd.read_csv('C:/Users/Arjun Janamatti/Downloads/WhatsApp Chat with DMB FAMILY.txt', sep=',')
#
# print(raw_df)

file_name = 'C:/Users/Arjun Janamatti/Downloads/WhatsApp Chat with DMB FAMILY.txt'

with open(file_name, encoding='utf8') as file:
    data = file.readlines()

print(data)

import re

data_2019_birthday, data_2020_birthday = [], []
for only in data:
    year_match = (re.findall(pattern=".*([\d]{1,2}/[\d]{1,2}/[1,9]{2})",string=only))
    if (len(year_match) > 0) & ("birthday" in only):
        data_2019_birthday.append(only)

for only_1 in data:
    year_match_1 = (re.findall(pattern=".*([\d]{1,2}/[\d]{1,2}/[0,2]{2})",string=only_1))
    if (len(year_match_1) > 0) & ("birthday" in only_1):
        data_2020_birthday.append(only_1)

print(data_2019_birthday)
print()
print(data_2020_birthday)