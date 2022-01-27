from numpy import sqrt, floor

def isprime(x):
    for k in range(2,floor(sqrt(x))+1):
        print(x,k,x%k)
        if x%k==0:
            return False
    return True
