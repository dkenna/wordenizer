import spacy
nlp = spacy.load('en')
doc = nlp(u'This is a sentence.')
print(doc.text)

for token in doc:
    print(token)
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
