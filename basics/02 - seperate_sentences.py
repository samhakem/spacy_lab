with open('/home/samhakem/PycharmProjects/spacy_lab/basics/data/alice.txt', 'r') as f:
    # Remove line breaks and double line breaks to allow
    # small 'model to accurately read in sentences with \n
    text = f.read().replace('\n\n', ' ').replace('\n', ' ')

ents = list(sentence.ents)  # Breaks down sentence object and turns it into a spaCy and will look for all named
