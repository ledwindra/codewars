def namelist(names):

    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        name = [x['name'] for x in names]
        name = [x if x != name[-1] else f'& {x}' for x in name]
        return ' '.join(name)
    name = [x['name'] for x in names]
    return ', '.join(name[ : -1]) + f' & {name[-1]}'