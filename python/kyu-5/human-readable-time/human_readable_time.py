def make_readable(seconds):

    string_conversion = lambda x: f'0{x}' if x < 10 else f'{x}'
    hour = string_conversion(int(seconds / 3600))
    minute = string_conversion(int((seconds % 3600) / 60))
    second = string_conversion(seconds % 60)
    output = f'{hour}:{minute}:{second}'
    
    return output