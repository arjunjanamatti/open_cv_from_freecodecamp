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




