import spacy
import pickle
import random
import pandas as pd

# with open('train_data.txt', 'r', encoding='utf-8') as file:
#     train_data = file.read()
#
#
# with open(file='train_data.pkl', mode = 'wb') as file:
#     pickle.dump(train_data, file)

try:
    with open(file='train_data.pickle', mode='rb') as file:
        word_list_df = pickle.load(file)
except:
    # df = pd.read_csv('train_data.txt', header=None)
    # word_list_df = [words for words in df.iloc[:, -1]]

    with open('train_data.txt', 'r', encoding='utf-8') as file:
        word_list_df = file.read()

    with open('train_data.pickle', mode='wb') as file:
        pickle.dump(word_list_df, file)

print(word_list_df)

# with open('train_data.pkl', 'rb', encoding='utf-8') as file:
#     train_data = file.read()
#
# print(train_data)