def is_prime(num):
    
    prime = []
        
    for i in range(2, num + 1):
        if i != num:
            prime.append(num % i)
    
    return 0 not in prime and num > 1