import nltk

grammar = nltk.CFG.fromstring("""
S -> V NP
V -> 'describe' | 'present'
NP -> PRP N
PRP -> 'your'
N -> 'work'
""")

parser = nltk.ChartParser(grammar)
sent = 'describe your work'.split()

print(list(parser.parse(sent)))
