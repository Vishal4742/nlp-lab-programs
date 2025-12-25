import nltk
nltk.download('punkt')
from nltk.util import ngrams

sampleText = 'this is a very good book to study'

for i in range(1, 4):
    NGRAMS = ngrams(sequence=nltk.word_tokenize(sampleText), n=i)
    for grams in NGRAMS:
        print(grams)
