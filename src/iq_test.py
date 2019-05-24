def iq_test(numbers):

    numbers = numbers.split()
    evenness = list()
    
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
        if numbers[i] % 2 == 0:
            evenness.append("even")
        else:
            evenness.append("odd")
            
    if evenness.count("odd") > 1:
        for i in range(len(numbers)):
            if numbers[i] % 2 == 0:
                numbers = numbers.index(numbers[i]) + 1
                break
    else:
        for i in range(len(numbers)):
            if numbers[i] % 2 != 0:
                numbers = numbers.index(numbers[i]) + 1
                break
            
    return numbers

if __name__ == "__main__":
    iq_test()