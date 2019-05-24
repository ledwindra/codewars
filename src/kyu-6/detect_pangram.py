def is_pangram(s=None):
    """
    Description:
    A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence 
    "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is 
    irrelevant).

    Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and 
    punctuation.    

    Example:

    """

    alphabet = list()

    for i in range(ord('a'), ord('z') + 1):
        alphabet.append(chr(i))
        
    s = s.lower()
    sentence_list = list(s)    
    pangram = list()

    for i in range(len(alphabet)):
        if alphabet[i] in sentence_list:
            pangram.append(alphabet[i])
        else:
            pass
        
    return len(pangram) == len(alphabet)

if __name__ == "__main__":
    is_pangram()