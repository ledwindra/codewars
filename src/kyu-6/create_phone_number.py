def create_phone_number(n=None):

    """
    Description:
    Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in 
    the form of a phone number.

    Examples:
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
    """
    
    for i in range(len(n)):
        n[i] = str(n[i])
    
    numlist = list()
    for i in [0, 3, 6]:
        if i != 6:
            numlist.append("".join(x for x in n[i : i+3]))
        else:
            numlist.append("".join(x for x in n[i : ]))
            
    return "({}) {}-{}".format(numlist[0], numlist[1], numlist[2])

if __name__ == "__main__":
    create_phone_number()    