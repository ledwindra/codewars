def printer_error():
    
    s = list(s)
    
    good_control = list()
    for i in range(ord("a"), ord("n")):
        good_control.append(chr(i))
    
    error_printer = list()
    for i in range(len(s)):
        if s[i] not in good_control:
            error_printer.append(1)
        else:
            pass
    
    error_printer = str(sum(error_printer)) + "/" + str(len(s))
    
    return error_printer

if __name__ == "__main__":
    printer_error()    