import Functions_module
num=int(input("Enter a number:"))
f=Functions_module.factors(num)
pf=Functions_module.prime_factors(num)
print("Factors:",f)
print("Prime Factors:",pf)
[25bcs138@mepcolinux ex4]$python3 mainpgm.py
Enter a number:12
Factors: [1, 2, 3, 4, 6, 12]
Prime Factors: [2, 2, 3]
[25bcs138@mepcolinux ex4]$cat set_module.py
def set_union(a,b):
    return a|b
def set_intersection(a,b):
    return a&b
def set_difference(a,b):
    return a-b
def set_symmetric_difference(a,b):
    return a^b
