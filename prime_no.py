def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def sum_of_two_primes(num):
    for i in range(2,num):
        if is_prime(i) and is_prime(num-i):
            print(num,"=",i,"+",(num-i))
            return True
    return False
n=int(input("Enter a number:"))
if sum_of_two_primes(n):
    print("Yes,it can be expressed as sum of two prime numbers")
else:
    print("No,it cannot be expressed as sum of two prime numbers")
