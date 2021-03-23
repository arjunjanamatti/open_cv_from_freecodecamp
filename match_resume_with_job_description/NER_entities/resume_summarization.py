import spacy
import pickle
import random
import pandas as pd
from ast import literal_eval

def GetEntities(text_file):
    try:
        df_1 = pd.read_pickle(f'{text_file}.pickle')
    except Exception as e:
        df = pd.read_csv(f'{text_file}.txt', sep='\n', header=None)
        df.to_pickle(f'{text_file}.pickle')
        df_1 = pd.read_pickle(f'{text_file}.pickle')


    content_list = [_ for _ in df_1.iloc[:, -1]]
    new_updated_list = []
    for j in range(len(content_list)):
        for i in ((literal_eval(content_list[j]))):
            new_updated_list.append(i)

    new_updated_list_1 = new_updated_list[1::2]
    return new_updated_list_1

text_file = 'train_data'
new_updated_list_1 = GetEntities(text_file)
print(new_updated_list_1)