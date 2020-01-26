def get_middle(s):
    
    odd = int((len(s) + 1) / 2)
    even = int(len(s) / 2)
    
    if len(s) % 2 != 0:
        return s[odd - 1]
    return s[even - 1 : even + 1]