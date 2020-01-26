def get_count(input_str):

    num_vowels = 0
    
    for vowel in ['a', 'e', 'i', 'u', 'o']:
        num_vowels += input_str.count(vowel)
    
    return num_vowels