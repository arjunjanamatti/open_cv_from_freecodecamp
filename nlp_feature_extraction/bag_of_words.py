import json
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

with open('intents.json') as file:
    data = json.load(file)

print(data)

words_corpus = []
sentence_list = []
labels_list = []


for dictionary in data['intents']:
    print(dictionary)
    print(dictionary['patterns'])
    print(dictionary['tag'])