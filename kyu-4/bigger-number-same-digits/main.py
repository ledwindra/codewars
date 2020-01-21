def next_bigger(n):

    to_list = [x for x in str(n)]
    to_list.sort()
    to_list.reverse()
    maximum = int(''.join(to_list))

    for i in range(n + 1, maximum + 1):
        output = [x for x in str(i)]
        output.sort()
        output.reverse()
        if output == to_list:
            return i
    return -1