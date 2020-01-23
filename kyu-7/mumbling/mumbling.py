def accum(s):

    output = []
    for i in range(len(s)):
        output.append(s[i].lower() * (i + 1))

    output = [x.capitalize() for x in output]
    output = '-'.join(output)

    return output