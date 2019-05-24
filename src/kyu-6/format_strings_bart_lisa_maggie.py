def namelist(names=None):
    """
    Description:
    Given: an array containing hashes of names

    Return: a string formatted as a list of names separated by commas except for the last two names, which should be 
    separated by an ampersand.

    Example:
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
    # returns 'Bart, Lisa & Maggie'

    namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
    # returns 'Bart & Lisa'

    namelist([ {'name': 'Bart'} ])
    # returns 'Bart'

    namelist([])
    # returns ''
    """
    
    nameval = list(names)

    if len(nameval) == 1:
        nameval = list(names[0].values())        
        names = "".join(x for x in nameval)
    elif len(nameval) == 2:
        nameval = list(names[0].values()) + list(names[1].values())
        names = " & ".join(x for x in nameval)
    else:
        nameval = list()

        for i in range(len(names)):
            names[i] = dict(names[i])
            names[i] = list(names[i].values())

            if names[i] == names[0]:
                nameval = nameval + names[i]
            elif names[i] == names[-1]:
                nameval = nameval + [" & "] + names[i]
            else:
                nameval = nameval + [", "] + names[i]

        names = "".join(x for x in nameval)       
    
    return names

if __name__ == "__main__":
    namelist()