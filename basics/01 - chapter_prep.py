with open('/home/samhakem/PycharmProjects/spacy_lab/data/alice.txt', 'r') as f:
    text = f.read()
    #print(text)
    chapters = text.split('CHAPTER ')[1:]  # Start from second index
    print(chapters[0])  # Print any chapter by indexing 0 = 1 etc
    #print(len(chapters))  # Confirm there are 12 chapters in book
