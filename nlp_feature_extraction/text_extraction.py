import pickle
import re
import pandas as pd


pickle_file_location = 'C:/Users/Arjun Janamatti/Downloads/data.pickle'

class get_personal_wish_messages:
    def __init__(self, pickle_file_location):
        self.pickle_file_location = pickle_file_location
        self.data_2019_birthday, self.data_2020_birthday = [], []
        self.arjun_wish_dict = {}
        pass

    def GetListFromTextMessages(self):
        '''
        First try to read the pickle file for all messages otherwise create a new pickle
        '''
        try:
            with open(file=pickle_file_location, mode='rb') as file_read:
                self.read_data = pickle.load(file_read)
        except:
            file_name = 'C:/Users/Arjun Janamatti/Downloads/WhatsApp Chat with DMB FAMILY.txt'

            with open(file_name, encoding='utf8') as file:
                data = file.readlines()

            self.read_data = [d.lower() for d in data]

            with open(pickle_file_location, 'wb') as file:
                pickle.dump(obj=self.read_data, file=file)


    def GetYearBirthdayWishes(self):
        self.GetListFromTextMessages()
        def get_data(dat):
            year_match_2019 = (re.findall(pattern=".*([\d]{1,2}/[\d]{1,2}/[1,9]{2})",string=dat))
            if (len(year_match_2019) > 0) & ("happy" in dat):
                self.data_2019_birthday.append(dat)
            year_match_2020 = (re.findall(pattern=".*([\d]{1,2}/[\d]{1,2}/[0,2]{2})",string=dat))
            if (len(year_match_2020) > 0) & ("happy" in dat):
                self.data_2020_birthday.append(dat)
            pass
        list(map(get_data, self.read_data))
        date, time, user_id, message = [], [], [], []

        def get_yearwise_data(partial_data):
            date.append((partial_data.split("-")[0]).split(",")[0])
            time.append((partial_data.split("-")[0]).split(",")[-1])
            user_id.append((partial_data.split("-")[-1]).split(":")[0])
            message.append((partial_data.split("-")[-1]).split(":")[-1])

        list(map(get_yearwise_data, self.data_2020_birthday))
        #
        self.raw_df_2020 = pd.DataFrame()
        self.raw_df_2020['date'] = date
        self.raw_df_2020['time'] = time
        self.raw_df_2020['user_id'] = user_id
        self.raw_df_2020['message'] = message

        return self.raw_df_2020

    def ProcessDataframe(self):
        self.GetYearBirthdayWishes()
        self.raw_df_2020.index = pd.to_datetime(self.raw_df_2020['date'])
        self.raw_df_2020.drop(labels='date', axis=1, inplace=True)
        # raw_df_2020.index = raw_df_2020['date']
        self.raw_df_2020['user_id'] = self.raw_df_2020['user_id'].apply(lambda x: x.strip())
        self.raw_df_2020['user_id'] = self.raw_df_2020['user_id'].apply(lambda x: x if "deepa" not in x else "null")
        self.raw_df_2020['user_id'] = self.raw_df_2020['user_id'].apply(lambda x: x if "munna" not in x else "null")
        self.raw_df_2020 = self.raw_df_2020[self.raw_df_2020['user_id'] != "null"]

        arjun_wishes = self.raw_df_2020[self.raw_df_2020['user_id'] == 'arjun janamatti']

        def remove_newline(row):
            regex = re.compile("[\n\r\t]")
            row = regex.sub("", row)
            return row

        self.arjun_wishes_1 = arjun_wishes.copy()
        self.arjun_wishes_1['message'] = arjun_wishes['message'].apply(lambda x: remove_newline(x))

    def GetDiciontaryWishes(self):
        self.ProcessDataframe()


        def get_wishes(rows):
            dates, messages = rows
            self.arjun_wish_dict[str(dates).split()[0]] = messages

        list(map(get_wishes, self.arjun_wishes_1[['message']].itertuples()))

        return self.arjun_wish_dict


    pass

result = get_personal_wish_messages(pickle_file_location)
result_dict = result.GetDiciontaryWishes()
print(result_dict)

# try:
#     with open(file=pickle_file_location, mode='rb') as file_read:
#         read_data = pickle.load(file_read)
# except:
#     file_name = 'C:/Users/Arjun Janamatti/Downloads/WhatsApp Chat with DMB FAMILY.txt'
#
#     with open(file_name, encoding='utf8') as file:
#         data = file.readlines()
#
#     print(data)
#
#     read_data = [d.lower() for d in data]
#
#     with open(pickle_file_location,'wb') as file:
#         pickle.dump(obj=read_data, file=file)
#
# data_2019_birthday, data_2020_birthday = [], []
# # def get_data(dat):
# #     year_match_2019 = (re.findall(pattern=".*([\d]{1,2}/[\d]{1,2}/[1,9]{2})",string=dat))
# #     if (len(year_match_2019) > 0) & ("happy" in dat):
# #         data_2019_birthday.append(only)
# #     year_match_2020 = (re.findall(pattern=".*([\d]{1,2}/[\d]{1,2}/[0,2]{2})",string=dat))
# #     if (len(year_match_2020) > 0) & ("happy" in dat):
# #         data_2020_birthday.append(only_1)
# #     pass
# #
# # list(map(get_data, read_data))
#
# for only in read_data:
#     year_match = (re.findall(pattern=".*([\d]{1,2}/[\d]{1,2}/[1,9]{2})",string=only))
#     if (len(year_match) > 0) & ("happy" in only):
#         data_2019_birthday.append(only)
#
# for only_1 in read_data:
#     year_match_1 = (re.findall(pattern=".*([\d]{1,2}/[\d]{1,2}/[0,2]{2})",string=only_1))
#     if (len(year_match_1) > 0) & ("happy" in only_1):
#         data_2020_birthday.append(only_1)
#
# print(data_2019_birthday)
# print(f'data_2019_birthday: {len(data_2019_birthday)}')
# print()
# print(f'data_2020_birthday: {len(data_2020_birthday)}')
# print(data_2020_birthday)
#
# date, time, user_id, message = [], [], [], []
#
# def get_yearwise_data(partial_data):
#     date.append((partial_data.split("-")[0]).split(",")[0])
#     time.append((partial_data.split("-")[0]).split(",")[-1])
#     user_id.append((partial_data.split("-")[-1]).split(":")[0])
#     message.append((partial_data.split("-")[-1]).split(":")[-1])
#     # return date, time, user_id, message
#
#
# # print(list(map(get_data, data_2020_birthday)))
# list(map(get_yearwise_data, data_2020_birthday))
# #
# raw_df_2020 = pd.DataFrame()
# raw_df_2020['date']  = date
# raw_df_2020['time']  = time
# raw_df_2020['user_id']  = user_id
# raw_df_2020['message']  = message
#
# raw_df_2020.index = pd.to_datetime(raw_df_2020['date'])
# raw_df_2020.drop(labels='date', axis=1, inplace=True)
# # raw_df_2020.index = raw_df_2020['date']
# raw_df_2020['user_id'] = raw_df_2020['user_id'].apply(lambda x: x.strip())
# raw_df_2020['user_id'] = raw_df_2020['user_id'].apply(lambda x: x if "deepa" not in x else "null")
# raw_df_2020['user_id'] = raw_df_2020['user_id'].apply(lambda x: x if "munna" not in x else "null")
# raw_df_2020 = raw_df_2020[raw_df_2020['user_id'] != "null"]
#
# arjun_wishes = raw_df_2020[raw_df_2020['user_id'] == 'arjun janamatti']
# print(raw_df_2020['user_id'].unique())
#
# def remove_newline(row):
#     regex = re.compile("[\n\r\t]")
#     row = regex.sub("", row)
#     return row
# arjun_wishes_1 = arjun_wishes.copy()
# arjun_wishes_1['message'] = arjun_wishes['message'].apply(lambda x: remove_newline(x))
#
# arjun_wish_dict = {}
# def get_wishes(rows):
#     dates, messages = rows
#     arjun_wish_dict[str(dates).split()[0]] = messages
#
# list(map(get_wishes, arjun_wishes_1[['message']].itertuples()))
# print(arjun_wish_dict)
# today = pd.to_datetime('today').floor('D')
# print(today)
#
#
# # for (dates, messages) in arjun_wishes[['message']].itertuples():
# #     print(str(dates).split()[0], messages)
#
#
# ##### GROUPY DATA BASED ON MONTH
# # # data_groupby = raw_df_2020.groupby(raw_df_2020.index.month)
# # data_groupby = raw_df_2020.groupby(raw_df_2020.index)
# # dates_dict = {}
# # for group in data_groupby.groups:
# #     dates_dict[group] = data_groupby.get_group(group)
# #
# # print(dates_dict)
#
#
#
#
#
#
# ##### USING NER
# # import spacy
# #
# # nlp = spacy.load("en_core_web_md")
# # print('loaded successfully')
# #
# # message_list = list(raw_df_2020['message'])
# # for mes in message_list:
# #     doc = nlp(mes)
# #     for ent in doc.ents:
# #         print(ent.text, ent.start_char, ent.end_char, ent.label_)
# #     print()