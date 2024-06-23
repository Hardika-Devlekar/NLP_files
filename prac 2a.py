from nltk.corpus import brown

print (brown.categories())

print (brown.words(categories='news'))

print (brown.words(fileids=['cg22']))

print (brown.sents(categories=['news', 'editorial', 'reviews']))
