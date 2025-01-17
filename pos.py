import nltk
from nltk.tokenize import word_tokenize

sentence = 'Harry and Marv went into a dumpster and visited a pizzeria while they were down there, and they got sick by getting well.'

words = nltk.word_tokenize(sentence)
words

for token in words:
    print(nltk.pos_tag([token]))