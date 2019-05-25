def is_prime(num=None):
    
    """
    Description:
    Define a function that takes one integer argument and returns true or false depending on if the integer is a prime.

    Define a function that takes one integer argument and returns logical value true or false depending on if the 
    integer is a prime.

    Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other 
    than 1 and itself.
    
    Assumptions:
    You can assume you will be given an integer input.
    You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).     
    """
    
    prime = []
        
    for i in range(2, num + 1):
        if i != num:
            prime.append(num % i)
    
    return 0 not in prime and num > 1

if __name__ == "__main__":
    is_prime()