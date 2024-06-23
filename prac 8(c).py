# Program to implement Snowball Stemmer
print("Name : Hardika Devlekar \tCollege : MLDC \tRoll No : 03")
import nltk
nltk.download('punkt')
from nltk.stem.snowball import SnowballStemmer
# Defining the stemmer
snowball_english = SnowballStemmer("english")
snowball_english = SnowballStemmer("dutch")
# Performing stemming on one word
print("\n1. Performing snowball stemming one word")
word = snowball_english.stem("Vibing")
print(word)
# Taking a list of english words
terms = ["Hardika", "cheerful", "bravery","drawing", "satisfactorily", "publisher", "painful", "hardworking",
"keys"]
# Performing stemming using snowball stemmer on words
print("\n2. Performing snowball stemming on a set of english language words")
for each_term in terms:
    print(snowball_english.stem(each_term))
# Taking a list of dutch words
# reeba = reeba, bessen = berries, vriendelijkheid = friendliness, hobbelig = bumpy
terms2 = ["Hardika", "bessen", "vriendelijkheid", "hobbelig"]
print("\n3. Performing snowball stemming on a set of dutch language words")
for each_term in terms2:
    print(snowball_english.stem(each_term))
