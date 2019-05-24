def persistence(n):
    """
    Description:

    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
    which is the number of times you must multiply the digits in num until you reach a single digit.

    Examples:
    persistence(39) => 3v# Because 3*9 = 27, 2*7 = 14, 1*4=4 # and 4 has only one digit.

    persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126, # 1*2*6 = 12, and finally 1*2 = 2.

    persistence(4) => 0 # Because 4 is already a one-digit number.    
    """
    
    step = 0
    
    while n >= 10:

        multiplier = 1
        nlist = list(str(n))

        for i in range(len(nlist)):
            nlist[i] = int(nlist[i])

        for i in nlist:
            multiplier = multiplier * i
            n = multiplier

        step += 1
    
    return step