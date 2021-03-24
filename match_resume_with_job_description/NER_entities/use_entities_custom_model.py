import spacy
import sys, fitz

nlp_model = spacy.load('nlp_model_1')

doc = fitz.open('damoder.pdf')
text = ''
for page in doc:
    text = text + str(page.getText())

text_join = "".join(text.split('\n'))
# # print(text_join)
doc = nlp_model(text_join)
# print(doc)
# print()
# print(doc.ents)
# print(nlp_model)
for ent in doc.ents:
    print(ent)
    print(f'{ent.label_.upper():{30}} - {ent.text}')

