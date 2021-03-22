import spacy
from spacy.vectors import Vectors
import os
import pandas as pd
import numpy as np
nlp = spacy.load('en_core_web_sm')
vectors = Vectors(shape=(10000, 300))
nlp.vocab.vectors = vectors
print(nlp.vocab.vectors.shape)
import re
re_c = re.compile(r'\w+')