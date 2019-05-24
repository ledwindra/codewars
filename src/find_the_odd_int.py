def find_it(seq):

    """
    Description:
    Given an array, find the int that appears an odd number of times.

    There will always be only one integer that appears an odd number of times.    
    """

    for i in range(min(seq), max(seq) + 1):
        if seq.count(i) % 2 != 0:
            odd = i
            break
            
    return odd

if __name__ == "__main__":
    find_it()    