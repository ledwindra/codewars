def accum(s):

    output = []
    for i in range(len(s)):
        output.append(s[i].lower() * (i + 1))

    for i in range(len(output)):
        output[i] = output[i].capitalize()

    output = '-'.join(output)

    return output