def persistence(n):

    step = 0
    while n >= 10:
        multiplier = 1
        array = [int(x) for x in str(n)]
        for i in array:
            multiplier *= i
            n = multiplier
        step += 1

    return step