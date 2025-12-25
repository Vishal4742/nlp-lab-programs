import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def chunk_sentence(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)

    grammar = r"""
        NP: {<DT|JJ|NN.*>+}          # Noun Phrase
        PP: {<IN><NP>}               # Prepositional Phrase
        VP: {<VB.*><NP|PP|CLAUSE>+$} # Verb Phrase
        CLAUSE: {<NP><VP>}           # Clause
    """

    parser = RegexpParser(grammar)
    chunked_sentence = parser.parse(tagged_words)

    return chunked_sentence

sentence = "The quick brown fox jumps over the lazy dog"
chunked_sentence = chunk_sentence(sentence)
print(chunked_sentence)
