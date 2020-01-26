def domain_name(url):
    
    begin = ['http://', 'https://', 'www.']
    i = 0
    while i < len(begin):
        if begin[i] in url:
            url = url.replace(begin[i], '')
        i += 1
    
    domain = ''
    for i in url:
        if i != '.':
            domain += i
        else:
            break
    
    return domain