import nltk
nltk.download('brown')
nltk.download('punkt')
from nltk.corpus import brown
from nltk import word_tokenize
from nltk import RegexpTagger
brown_sents = brown.sents(categories = 'news')
brown_tagged_sents = brown.tagged_sents(categories = 'news')
import nltk
nltk.download('brown')
nltk.download('punkt')
from nltk.corpus import brown
from nltk import word_tokenize
from nltk import RegexpTagger
brown_sents = brown.sents(categories = 'news')
brown_tagged_sents = brown.tagged_sents(categories = 'news')
patterns = [
(r'.*ing$', 'VBG'), # gerunds
(r'.*ed$', 'VBD'), # simple past
(r'.*es$', 'VBZ'), # 3rd singular present
(r'.*ould$', 'MD'), # modals
(r'.*\'s$', 'NN$'), # possessive nouns
(r'.*s$', 'NNS'), # plural nouns
(r'^-?[0-9]+(\.[0-9]+)?$', 'CD'), # cardinal numbers
(r'.*', 'NN') # nouns (default)
]
regexp_tagger = nltk.RegexpTagger(patterns)
print (regexp_tagger.tag(brown_sents[3]))
