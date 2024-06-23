from nltk.corpus.reader import WordListCorpusReader

reader_corpus = WordListCorpusReader('.', ['C:/Users/Devlekar/OneDrive/Documents/D Drive/MSCIT Part -2 Sem 4/Assignments & Practicals/NLP Pracs/wordfile.txt'])

print (reader_corpus.words())
