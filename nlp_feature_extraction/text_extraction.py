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

data = [d.lower() for d in data]

import re

data_2019_birthday, data_2020_birthday = [], []
for only in data:
    year_match = (re.findall(pattern=".*([\d]{1,2}/[\d]{1,2}/[1,9]{2})",string=only))
    if (len(year_match) > 0) & ("happy" in only):
        data_2019_birthday.append(only)

for only_1 in data:
    year_match_1 = (re.findall(pattern=".*([\d]{1,2}/[\d]{1,2}/[0,2]{2})",string=only_1))
    if (len(year_match_1) > 0) & ("happy" in only_1):
        data_2020_birthday.append(only_1)

print(data_2019_birthday)
print(f'data_2019_birthday: {len(data_2019_birthday)}')
print()
print(f'data_2020_birthday: {len(data_2020_birthday)}')
print(data_2020_birthday)

date, time, user_id, message = [], [], [], []

print(f'date: {(data_2020_birthday[0].split("-")[0]).split(",")[0]}, time: {(data_2020_birthday[0].split("-")[0]).split(",")[-1]}, '
      f'user_id: {(data_2020_birthday[0].split("-")[-1]).split(":")[0]}, message: {(data_2020_birthday[0].split("-")[-1]).split(":")[-1]}' )
