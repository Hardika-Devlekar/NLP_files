# Program to implement Lancaster Stemmer
print("Name : Hardika Devlekar \tCollege : MLDC \tRoll No : 03")
import nltk
nltk.download('punkt')
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
# Defining the stemmer
lancaster = LancasterStemmer()
# Taking words which have a similar stem
terms = ["enjoy", "enjoying", "enjoyed", "enjoyable", "enjoyment", "enjoyful"]
# Performing stemming using lancaster stemmer on words
print("\n1. Performing lancaster stemming on the words")
for each_term in terms:
    print(lancaster.stem(each_term))
    # Taking a sentence
    sentence = "Heya Hardika, Why is it so with the dancers that when dancers dance, they dance as if they are dancing in the air?"
# Performing stemming using lancaster stemmer on a sentence
print("\n2. Performing lancaster stemming on a sentence")
words = word_tokenize(sentence, language = 'english')
for each_word in words:
    print(lancaster.stem(each_word))
    # Performing stemming using lancaster stemmer on a text file
    print("\n3. Performing lancaster stemming on a text file - one sentence at a time")
# Treating the text file as a collection of sentences
reeba_file = open("read.txt")
my_lines_list = reeba_file.readlines()
# Accessing one line at a time from the text file
words = word_tokenize(my_lines_list[0], language = 'english')
for each_word in words:
    print(lancaster.stem(each_word))
