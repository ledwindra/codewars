from string import punctuation

def shorten_to_date(long_date):

    punclist = list(punctuation)
    long_date_list = list(long_date)
    long_date = list()
    
    for i in range(len(long_date_list)):
        if long_date_list[i] not in punclist:
            long_date.append(long_date_list[i])
        else:
            break
    
    short_date = "".join(x for x in long_date)
    
    return short_date 