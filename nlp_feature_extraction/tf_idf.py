import json
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize
import numpy as np
import pickle

# load the json file like a dictionary
with open('intents.json') as file:
    data = json.load(file)


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


# lower case all the words in corpus
words_corpus = [words.lower() for words in words_corpus]

# remove '?' from the corpus list
words_corpus = [words for words in words_corpus if words != '?']

# lemmatize each word in corpus
lemma = WordNetLemmatizer()
words_corpus = [lemma.lemmatize(words) for words in words_corpus]

# only unique words and order the corpus list
words_corpus = sorted(list(set(words_corpus)))

# here the labels have to be created, hence first will create empty labels and based on the label will fill up as binary bag of words
labels_empty = [0 for _ in range(len(labels_list))]

labels_empty_nested = []
term_frequency_nested = []

def dict_value_count(list_1):
    element_count = {}
    for element in list_1:
        # checking whether it is in the dict or not
        if element in element_count:
            # incerementing the count by 1
            element_count[element] += 1
        else:
            # setting the count to 1
            element_count[element] = 1
    return element_count, len(list_1)

for index, sentence in enumerate(sentence_list):
    terms_frequency = []

    sentence_lemma = [lemma.lemmatize(words) for words in sentence]

    sentence_lemma = [words.lower() for words in sentence_lemma]

    # term frequency
    # print(sorted(sentence_lemma))
    print(sentence_lemma)
    word_dict, total_words_sentence = dict_value_count(sentence_lemma)

    for words in word_dict:
        # print(words)
        # if word in the sentence in the corpus, add 1 else 0
        if words in words_corpus:
            print(words, int(word_dict[words])/int(total_words_sentence))
            terms_frequency.append(int(word_dict[words])/int(total_words_sentence))
        else:
            print(words, 0)
            terms_frequency.append(0)
    #
    # # now for the labels, based on the label add 1 or 0
    # labels_empty_copy = labels_empty[:]
    # labels_empty_copy[labels_list.index(sentence_labels_list[index])] = 1
    # labels_empty_nested.append(labels_empty_copy)
    term_frequency_nested.append(terms_frequency)

# # convert list to numpy array
# features_nested = np.array(features_nested)
# labels_empty_nested = np.array(labels_empty_nested)
#
# with open(file='data.pickle', mode='wb') as file:
#     pickle.dump(obj=(words_corpus, labels_list, features_nested, labels_empty_nested), file=file)