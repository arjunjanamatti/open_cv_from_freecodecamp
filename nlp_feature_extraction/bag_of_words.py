import json
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize
import numpy as np

# load the json file like a dictionary
with open('intents.json') as file:
    data = json.load(file)

print(data)

words_corpus = []
sentence_list = []
labels_list = []
sentence_labels_list = []


for dictionary in data['intents']:
    labels_list.append(dictionary['tag'])
    for sentences in dictionary['patterns']:
        tokenized_sentences = (word_tokenize(text=sentences))
        sentence_list.append(tokenized_sentences)
        sentence_labels_list.append(dictionary['tag'])
        words_corpus.extend(tokenized_sentences)



print(sentence_list)
print(sentence_labels_list)

# lower case all the words in corpus
words_corpus = [words.lower() for words in words_corpus]

# remove '?' from the corpus list
words_corpus = [words for words in words_corpus if words != '?']
print(len(words_corpus))

# lemmatize each word in corpus
lemma = WordNetLemmatizer()
words_corpus = [lemma.lemmatize(words) for words in words_corpus]

# only unique words and order the corpus list
words_corpus = sorted(list(set(words_corpus)))
print(len(words_corpus))

# here the labels have to be created, hence first will create empty labels and based on the label will fill up as binary bag of words
labels_empty = [0 for _ in range(len(labels_list))]
print(labels_empty)
labels_empty_nested = []
features_nested = []
for index, sentence in enumerate(sentence_list):
    features_list = []

    sentence_lemma = [lemma.lemmatize(words) for words in sentence]
    for words in sentence_lemma:
        # if word in the sentence in the corpus, add 1 else 0
        if words in words_corpus:
            features_list.append(1)
        else:
            features_list.append(0)

    # now for the labels, based on the label add 1 or 0
    labels_empty_copy = labels_empty[:]
    labels_empty_copy[labels_list.index(sentence_labels_list[index])] = 1
    labels_empty_nested.append(labels_empty_copy)
    features_nested.append(features_list)

# convert list to numpy array
features_nested = np.array(features_nested)
labels_empty_nested = np.array(labels_empty_nested)
