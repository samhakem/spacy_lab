import spacy
# import os

with open('/home/samhakem/PycharmProjects/spacy_lab/basics/data/alice.txt', 'r') as f:
    # Remove line breaks and double line breaks to allow
    # small 'model to accurately read in sentences with \n
    text = f.read().replace('\n\n', ' ').replace('\n', ' ')

    # print(text)
    chapters = text.split('CHAPTER ')[1:]  # Start from second index
    # print(chapters[0])  # Print any chapter by indexing 0 = 1 etc
    # print(len(chapters))  # Confirm there are 12 chapters in book
    # print(os.getcwdu())  # Confirm working directory for f reads

chapter1 = chapters[0]

nlp = spacy.load('en_core_web_sm')

# Calling doc object and assigning nlp object to chapter1
doc = nlp(chapter1)

# Separate out doc out by sents
sentences = list(doc.sents)
sentence = (sentences[2])
# print(sentences[1])

ents = list(sentence.ents)  # Breaks down sentence object and turns it into a spaCy and will look for all named
# ents = list(doc.ents)  # Test and deal with false positives across whole doc
# entities in text

people = []

for ent in ents:
    if ent.text.label_ == 'PERSON':
        people.append(ent)

print(people)

print(ents[0].label)  # [Alice] Numerical value of object
print(ents[0].label_)  # [PERSON] Actual entity
print(ents[0].text)  # Object string
