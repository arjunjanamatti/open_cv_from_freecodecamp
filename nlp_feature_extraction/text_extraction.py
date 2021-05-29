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
import pandas as pd

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

def get_data(partial_data):
    date.append((partial_data.split("-")[0]).split(",")[0])
    time.append((partial_data.split("-")[0]).split(",")[-1])
    user_id.append((partial_data.split("-")[-1]).split(":")[0])
    message.append((partial_data.split("-")[-1]).split(":")[-1])
    # return date, time, user_id, message


# print(list(map(get_data, data_2020_birthday)))
list(map(get_data, data_2020_birthday))
#
raw_df_2020 = pd.DataFrame()
raw_df_2020['date']  = date
raw_df_2020['time']  = time
raw_df_2020['user_id']  = user_id
raw_df_2020['message']  = message
print(raw_df_2020)
raw_df_2020.to_csv('raw_df_2020.csv')

