import string

ALPHABET = string.ascii_lowercase

def is_pangram(sentence):

    sentence = sentence.lower()

    return len(set([x in sentence for x in ALPHABET])) == 1