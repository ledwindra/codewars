def create_phone_number(n):

    start = ''.join([str(x) for x in n[ : 3]])
    mid = ''.join([str(x) for x in n[3 : 6]])
    end = ''.join([str(x) for x in n[6 : ]])
            
    return f'({start}) {mid}-{end}'