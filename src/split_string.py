def solution(s=None):

    """
    Description:
    
    Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd 
    number of characters then it should replace the missing second character of the final pair with an underscore ('_').

    Examples:

    solution('abc') # should return ['ab', 'c_']
    solution('abcdef') # should return ['ab', 'cd', 'ef']        
    """

    slist = list()
    
    for i in range(len(s)):
        slist.append(s[2 * i : 2 * (i + 1)])
        
        if slist[i] in ['']:
            slist.pop()
            break
    
    if len(s) % 2 != 0:
        slist[-1] = slist[-1] + '_'
        
    return slist

if __name__ == "__main__":
    solution()    