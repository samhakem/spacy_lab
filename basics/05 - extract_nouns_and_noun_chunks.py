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
sentences = list(doc.sents)
sentence = (sentences[2])

nouns = []

for token in sentence:
    if token.pos_ == 'NOUN':  # Run with nouns or
    # if token.pos_ == 'ADV':  # run with adverbs etc, you can run with any pos_
        nouns.append(token)

# print(nouns)

# print(list(doc.noun_chunks))

# Extract specific string/noun in text
chunks = (list(doc.noun_chunks))
for chunk in chunks:
    if 'watch' in str(chunk):
        print(chunk)
