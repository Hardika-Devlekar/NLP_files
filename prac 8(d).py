# Program to implement RegExp Stemmer
print("Name : Hardika Devlekar \tCollege : MLDC \tRoll No : 03")
import nltk
nltk.download('punkt')
from nltk.stem import RegexpStemmer
# Defining the stemmer
regexp = RegexpStemmer('ing$|s$|e$|able$|ment$|less$|ly$', min=4)
# Performing stemming one word
print("\n1. Performing regexp stemming on one word at a time")
print(regexp.stem('cars'))
print(regexp.stem('bee'))
print(regexp.stem('compute'))
# Taking a list of word
terms = ["Hardika", "stemming", "mentally", "ease","rockstar", "frictionless", "management","flowers",
"advisable"]
# Performing stemming using lancaster stemmer on words
print("\n2. Performing regexp stemming on a list of words")
for each_term in terms:
    print(regexp.stem(each_term))
