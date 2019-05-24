def find_uniq(arr=None):
    """
    There is an array with some numbers. All numbers are equal except for one. Try to find it!

    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    It’s guaranteed that array contains more than 3 numbers.
    """

    arr.sort()
    n = list()
    
    if arr[0] != arr[1]:
        n = arr[0]
    elif arr[-1] != arr[-2]:
        n = arr[-1]
    else:
        pass
        
    return n

if __name__ == "__main__":
    find_uniq()    