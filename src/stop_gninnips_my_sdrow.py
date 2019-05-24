def spin_words(sentence=None):
    
    """
    Description:
    Write a function that takes in a string of one or more words, and returns the same string, but with all five or 
    more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and 
    spaces. Spaces will be included only when more than one word is present.

    Examples:
    spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
    spinWords( "This is a test") => returns "This is a test" 
    spinWords( "This is another test" )=> returns "This is rehtona test"
    """

    
    sentence_list = sentence.split()
    
    for i in range(len(sentence_list)):
        if len(sentence_list[i]) >= 5:
            sentence_list[i] = "".join(reversed(sentence_list[i]))
        else:
            pass
            
    sentence = " ".join(x for x in sentence_list)

    return sentence

if __name__ == "__main__":
    spin_words()    