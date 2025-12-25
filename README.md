# NLP Lab Programs

This repository contains 10 Python programs based on the NLP Lab Manual from Oriental College of Technology, Bhopal.

## Programs List

1. **program1_tokenization.py** - Word and sentence tokenization using NLTK
2. **program2_pos_tagging.py** - Parts of Speech (POS) tagging
3. **program3_lemmatization.py** - Text lemmatization
4. **program4_chunking.py** - Syntactic chunking (NP, VP, PP, etc.)
5. **program5_cyk_parsing.py** - CYK/Chart parsing with context-free grammar
6. **program6_ngrams.py** - Finding unigrams, bigrams, and trigrams
7. **program7_language_model_probability.py** - Bigram language model probability calculation
8. **program8_stopwords.py** - Stopword removal
9. **program9_stemming.py** - Text stemming using Porter Stemmer
10. **program10_ner.py** - Named Entity Recognition (NER)

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. The programs will automatically download required NLTK data on first run.

## Usage

Run any program individually:

```bash
python program1_tokenization.py
python program2_pos_tagging.py
# ... and so on
```

## Requirements

- Python 3.6+
- NLTK library
- Required NLTK data (downloaded automatically):
  - punkt (tokenizer)
  - averaged_perceptron_tagger (POS tagger)
  - wordnet (lemmatizer)
  - stopwords (stopword list)
  - maxent_ne_chunker (NER)
  - words (word list)

## Course Information

- **Institution**: Oriental College of Technology, Bhopal
- **Department**: CSE-AIML
- **Course**: Natural Language Processing (AL-504(B))
- **Program**: B.Tech, Semester V

## Notes

- All programs are based on the lab manual specifications
- Programs include example outputs and explanations
- Some programs may require additional setup (e.g., tkinter for parse tree visualization)

