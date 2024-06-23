from nltk.corpus import wordnet

# Retrieve synsets for the word "active"
# retrieves all the synsets (sets of cognitive synonyms) for the word "active". A synset contains a group of synonyms that share a common meaning. The result is a list of synsets.
print( wordnet.synsets("active"))

# Find antonyms for a specific lemma
print(wordnet.lemma('active.a.01.active').antonyms())#This retrieves a specific lemma (a word form with a specific sense) from the synset active.a.01. Here, 'active' is the lemma name, 'a' stands for adjective, and '01' is the sense number.
