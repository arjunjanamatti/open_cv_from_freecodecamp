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

raw_df_2020.index = pd.to_datetime(raw_df_2020['date'])
raw_df_2020.drop(labels='date', axis=1, inplace=True)
# raw_df_2020.index = raw_df_2020['date']
raw_df_2020['user_id'] = raw_df_2020['user_id'].apply(lambda x: x if "deepa" not in x else "null")
raw_df_2020['user_id'] = raw_df_2020['user_id'].apply(lambda x: x if "munna" not in x else "null")
raw_df_2020 = raw_df_2020[raw_df_2020['user_id'] != "null"]

# data_groupby = raw_df_2020.groupby(raw_df_2020.index.month)
data_groupby = raw_df_2020.groupby(raw_df_2020.index)
dates_dict = {}
for group in data_groupby.groups:
    dates_dict[group] = data_groupby.get_group(group)

print(dates_dict)

import spacy

nlp = spacy.load("en_core_web_md")
print('loaded successfully')

message_list = list(raw_df_2020['message'])
for mes in message_list:
    doc = nlp(mes)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    print()