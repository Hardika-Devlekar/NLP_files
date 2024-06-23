import nltk
from nltk import tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')

para = "And now we are going to learn something new"
sents = tokenize.sent_tokenize(para)
print("\nsentence tokenization\n===================\n",sents)

# word tokenization
print("\nword tokenization\n===================\n")
for index in range(len(sents)):
  words = tokenize.word_tokenize(sents[index])
  print(nltk.pos_tag(words))

import nltk
nltk.corpus.brown.tagged_words()
nltk.download('treebank')
nltk.corpus.treebank.tagged_words()
nltk.download('universal_tagset')
from nltk.corpus import brown
noundist = nltk.FreqDist(w2 for ((w1, t1), (w2, t2)) in
      nltk.bigrams(brown.tagged_words(tagset="universal"))
      if w1.lower() == "the" and t2 == "NOUN")
print (noundist.most_common(10))
