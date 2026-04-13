def factors(n):
    factor=[]
    for i in range(1,n+1):
        if n%i==0:
            factor.append(i)
    return factor
def prime_factors(n):
    prime_factor=[]
    i=2
    while i<=n:
        if n%i==0:
            prime_factor.append(i)
            n=n//i
        else:
            i+=1
    return prime_factor
