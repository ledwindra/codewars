def move_zeros(array):

    array_str = [str(x) for x in array]
    total_zero = array_str.count(0)
    for i in range(len(array)):
        if array_str[i] == '0':
            array.append(0)
    
    if total_zero > 0:
        for i in range(total_zero):
            array.remove(0)
    else:
        return array

    return array