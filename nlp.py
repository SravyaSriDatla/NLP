import os
import nltk
#nltk.download()

import nltk.corpus

from nltk.tokenize import word_tokenize

AI = '''Artificial Intelligence refers to the intelligence of machines. This is in contrast to the natural intelligence of
humans and animals. With Artificial Intelligence, machines perform functions such as learning, planning, reasoning and
problem-solving. Most noteworthy, Artificial Intelligence is the simulation of human intelligence by machines.
It is probably the fastest-growing development in the World of technology and innovation. Furthermore, many experts believe
AI could solve major challenges and crisis situations.'''

from nltk.tokenize import word_tokenize

AI_tokens = word_tokenize(AI)
AI_tokens

from nltk.tokenize import sent_tokenize

AI_sent = sent_tokenize(AI)
AI_sent

from nltk.tokenize import blankline_tokenize

AI_blank = blankline_tokenize(AI)
AI_blank

from nltk.tokenize import WhitespaceTokenizer

AI_white = WhitespaceTokenizer().tokenize(AI)
AI_white

s = 'Good apple cost $3.88 in hyderbad. Please buy me two of them. Thanks.'
s

from nltk.tokenize import wordpunct_tokenize
word_punct = wordpunct_tokenize(AI)

# bigrams, trigrams, ngrams

from nltk.util import ngrams , trigrams, bigrams

string = 'hello the best and most beautifull thing in the world cannot be seen or even touched,they must be felt with heart'
wtokens = word_tokenize(string)

qbigram = list(nltk.bigrams(wtokens))

qtrigram = list(nltk.trigrams(wtokens))

q_ngram = list(nltk.ngrams(wtokens, 5))

#Stemming

from nltk.stem import PorterStemmer

pst = PorterStemmer()

print(pst.stem('Affection'))

words_to_stem = ['give', 'gave', 'given', 'giving', 'thinking', 'loving', 'maximum']

for word in words_to_stem:
    print(word +' : '+ pst.stem(word))
    
#lancaster Stemmer
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
for word in words_to_stem:
    print(word +' : '+ lst.stem(word))
    
#Snowball Stemmer
from nltk.stem import SnowballStemmer

sbst = SnowballStemmer('english')
for word in words_to_stem:
    print(word +' : '+ sbst.stem(word))
    
# Lemmetization

from nltk.stem import wordnet, WordNetLemmatizer

word_lem = WordNetLemmatizer()

for word in words_to_stem:
    print(word +' : '+ word_lem.lemmatize(word))

