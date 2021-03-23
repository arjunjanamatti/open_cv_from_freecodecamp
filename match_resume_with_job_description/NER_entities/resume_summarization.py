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

    annotation_list = new_updated_list[1::2]
    text_list = new_updated_list[1::2]
    return text_list, annotation_list

text_file = 'train_data'
text_list, annotation_list = GetEntities(text_file)

for ann in annotation_list:
    for ent in ann['entities']:
        print(ent[0], ent[2])

