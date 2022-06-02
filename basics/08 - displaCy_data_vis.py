import spacy
from spacy import displacy

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
# doc = nlp(chapter1)  # Individual chapters
doc = nlp(text)  # Entire text
sentences = list(doc.sents)
sentence = (sentences[6])

# Individual sentence
# html = displacy.render(sentence, style='dep')  # Render saves the visualisation, dep displays dependency parse
# html = displacy.render(sentence, style='ent')  # Entity recognition

# Entire document
# html = displacy.render(doc, style='dep')  # Render saves the visualisation, dep displays dependency parse
html = displacy.render(doc, style='ent')  # Entity recognition

# html = displacy.serve(sentence, style='dep')  # Serve only displays it

with open('data_vis.html', 'w') as f:  # Saves the visualization to an HTML file locally
    f.write(html)
