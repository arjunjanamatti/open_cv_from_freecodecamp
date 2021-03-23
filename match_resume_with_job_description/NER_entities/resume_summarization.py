import spacy
import pickle
import random

# with open('train_data.txt', 'r', encoding='utf-8') as file:
#     train_data = file.read()
#
#
# with open(file='train_data.pkl', mode = 'wb') as file:
#     pickle.dump(train_data, file)

with open('train_data.pkl', 'rb', encoding='utf-8') as file:
    train_data = file.read()

print(train_data)