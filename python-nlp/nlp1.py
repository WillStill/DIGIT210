import spacy
#nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

chatPrompt = open('stiller-chatgpt2-3.txt', 'r', encoding='utf8')
words = chatPrompt.read()
#wordstrings = str(words)
#print(wordstrings)

nlp = spacy.load("en_core_web_sm")
doc = nlp(words)

#print("My collections of NOUNs and VERBs :)")
#for token in doc:
    #print(token.pos_)
    #if token.pos_ == "NOUN":
        #print(token.text,"---", "It's a NOUN! :O")
    #if token.pos_ == "VERB":
        #print(token.text,"---", "This verb is cool ig")

#What if we had just the nouns, propernouns, verbs, and AUX?
for token in doc:
    if token.pos_ == "NOUN":
        print(token.text, end=' ')
    if token.pos_ == "PROPN":
        print(token.text, end=' ')
    if token.pos_ == "VERB":
        print(token.text, end=' ')
    if token.pos_ == "AUX":
        print(token.text, end=' ')
#Kinda understandable I guess?

#What if it was just the lemmas?
print("\n Only lemmas now:")
for token in doc:
    if token.pos_ == "NOUN":
        print(token.lemma_, end=' ')
    if token.pos_ == "PROPN":
        print(token.lemma_, end=' ')
    if token.pos_ == "VERB":
        print(token.lemma_, end=' ')
    if token.pos_ == "AUX":
        print(token.lemma_, end=' ')
#much worse :)