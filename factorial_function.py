def factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result
n=int(input("Enter a no.:"))
print("Factorials from 1 to",n,":")
for i in range(1,n+1):
    print(i,"!=",factorial(i))
