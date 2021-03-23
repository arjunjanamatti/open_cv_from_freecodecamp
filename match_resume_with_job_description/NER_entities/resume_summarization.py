import spacy
import pickle
import random
import pandas as pd
from ast import literal_eval

# df = pd.read_csv('train_data.txt', sep='\n', header=None)
#
# df.to_pickle('train_data.pickle')

# content_list = [_ for _ in df.iloc[:,-1]]
# with open('train_data.pickle', 'wb') as file:
#     pickle.dump(content_list,file)

df_1 = pd.read_pickle('train_data.pickle')

content_list = [_ for _ in df_1.iloc[:,-1]]
print(len(content_list[0]))
print(((literal_eval(content_list[0])))[0])
print(((literal_eval(content_list[0])))[1])
new_updated_list = []
for j in range(len(content_list)):
    for i in  ((literal_eval(content_list[j]))):
        new_updated_list.append(i)

print(new_updated_list[1])