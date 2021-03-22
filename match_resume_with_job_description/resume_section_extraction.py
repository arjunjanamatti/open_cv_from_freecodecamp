import spacy
from spacy.vectors import Vectors
import os
import pandas as pd
import numpy as np
nlp = spacy.load('en_core_web_md')
vectors = Vectors(shape=(10000, 300))
nlp.vocab.vectors = vectors
print(nlp.vocab.vectors.shape)
import re
re_c = re.compile(r'\w+')

# switch for debug
flag_print = True

# switch to clear existing data
flag_clear = True

#threshold value for determining section
threshold = 0.5

# to get extract sections from the resume -- add or remove from  'similar_to' accordingly
similar_to = {
    'edu': ['education', 'study', 'academics', 'institute', 'school', 'college'],
    'exp': ['job', 'internship', 'training', 'research', 'career', 'profession', 'role'
                                                                                 'project', 'responsibility',
            'description', 'work experience', 'workshop', 'conference'],
    'skill': ['skill', 'languages', 'technology', 'framework', 'tools', 'database'],
    'extra': ['introduction', 'intro', 'achievement', 'hobby', 'links', 'additional',
              'personal', 'award', 'objective', 'miscellaneous', 'interest', 'certificates']
}

list_of_sections = similar_to.keys()

# to bring similar_words to their normal forms
for section in list_of_sections:
    new_list = []

    for word in similar_to[section]:
        docx = nlp(word)
        new_list.append(docx[0].lemma_)

    if flag_print:
        print(section, new_list)

    similar_to[section] = new_list


# function to remove unnecessary symbols and stopwords
def modify(word):
    try:
        symbols = '''~'`!@#$%^&*)(_+-=}{][|\:;",./<>?'''
        mod_word = ''

        for char in word:
            if (char not in symbols):
                mod_word += char.lower()

        docx = nlp(mod_word)

        if (len(mod_word) == 0 or docx[0].is_stop):
            return None
        else:
            return docx[0].lemma_
    except:
        return None  # to handle the odd case of characters like 'x02', etc.


# utility function to skip line when no alphabet present
def is_empty(line):
    for c in line:
        if (c.isalpha()):
            return False
    return True


dict_of_data_series = {}
flag_print = False

for file_name in os.listdir(os.getcwd() + '/resume_text'):
    if flag_print:
        print('\n')
        print('*' * 25)
        print(file_name)
        print('*' * 25)

    main_file_handler = open('resume_text/' + file_name, 'r', encoding='utf-8')
    previous_section = 'extra'

    curr_data_series = pd.Series([""] * len(list_of_sections), index=list_of_sections)

    for line in main_file_handler:
        # skip line if empty
        if (len(line.strip()) == 0 or is_empty(line)):
            continue

        # processing next line
        list_of_words_in_line = re_c.findall(line)
        list_of_imp_words_in_line = []

        for i in range(len(list_of_words_in_line)):
            modified_word = modify(list_of_words_in_line[i])

            if (modified_word):
                list_of_imp_words_in_line.append(modified_word)

        curr_line = ' '.join(list_of_imp_words_in_line)
        doc = nlp(curr_line)
        section_value = {}

        # initializing section values to zero
        for section in list_of_sections:
            section_value[section] = 0.0
        section_value[None] = 0.0

        # updating section values
        for token in doc:
            for section in list_of_sections:
                for word in similar_to[section]:
                    word_token = doc.vocab[word]
                    section_value[section] = max(section_value[section], float(word_token.similarity(token)))

        # determining the next section based on section values and threshold
        most_likely_section = None
        for section in list_of_sections:
            # print '>>', section, section_value[section]
            if (section_value[most_likely_section] < section_value[section] and section_value[section] > threshold):
                most_likely_section = section

        # updating the section
        if (previous_section != most_likely_section and most_likely_section is not None):
            previous_section = most_likely_section

        # writing data to the pandas series
        try:
            docx = nlp(line)
        except:
            continue  # to handle the odd case of characters like 'x02', etc.
        mod_line = ''
        for token in docx:
            if (not token.is_stop):
                mod_line += token.lemma_ + ' '

        curr_data_series[previous_section] += mod_line

    dict_of_data_series[file_name] = curr_data_series
    if flag_print:
        print(curr_data_series)
    main_file_handler.close()

data_frame = pd.DataFrame(dict_of_data_series)
data_frame.to_csv('prc_data.csv', sep='\t')
# data_frame.head()

