# Program to implement Porter Stemmer
print("Name : Hardika Devlekar \tCollege : MLDC \tRoll No : 03")
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
# Defining the stemmer
porter = PorterStemmer()
# Taking words which have a similar stem
terms = ["gene", "genes", "genesis", "genetic", "generic", "general"]
# Performing stemming using porter stemmer on words
print("\n1. Performing porter stemming on the words")
for each_term in terms:
    print(porter.stem(each_term))
    # Taking a sentence
    sentence = "Heya Hardika, do you know it is important to be pythonly while pythoning with python language. Stay being a pythoner"
    # Performing stemming using porter stemmer on a sentence
    print("\n2. Performing porter stemming on a sentence")
    words = word_tokenize(sentence, language = 'english')
    for each_word in words:
        print(porter.stem(each_word))
