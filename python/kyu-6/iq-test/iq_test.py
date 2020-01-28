def iq_test(numbers):
    
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]
    
    if len(even) == 1:
        unique = even
    else:
        unique = odd
    
    return numbers.index(unique[0]) + 1