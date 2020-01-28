def dig_pow(n, p):

    array = [int(x) for x in str(n)]
    array = sum([array[x] ** (p + x) for x in range(len(array))])

    if array % n == 0:
        return int(array / n)
    return -1