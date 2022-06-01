import spacy
import os

with open('/home/samhakem/PycharmProjects/spacy_lab/basics/data/alice.txt', 'r') as f:
    text = f.read()
    #print(text)
    chapters = text.split('CHAPTER ')[1:]  # Start from second index
    print(chapters[0])  # Print any chapter by indexing 0 = 1 etc
    #print(len(chapters))  # Confirm there are 12 chapters in book
    #print(os.getcwd())  # Confirm working directory for f reads

nlp = spacy.load('en_core_web_sm')
