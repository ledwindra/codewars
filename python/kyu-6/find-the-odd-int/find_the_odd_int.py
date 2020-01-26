def find_it(seq):

    unique_num = list(set(seq))
    occurence = [seq.count(x) for x in unique_num]
    
    return [unique_num[x] for x in range(len(occurence)) if occurence[x] % 2 != 0][0]