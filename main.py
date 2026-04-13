import set_module
set1=set(map(int,input("Enter elements of set1:").split()))
set2=set(map(int,input("Enter elements of set2:").split()))
print("Union:",set_module.set_union(set1,set2))
print("Intersection:",set_module.set_intersection(set1,set2))
print("Difference:",set_module.set_difference(set1,set2))
print("Symmetric Difference:",set_module.set_symmetric_difference(set1,set2))
[25bcs138@mepcolinux ex4]$python3 main.py
Enter elements of set1:1 2 3 4
Enter elements of set2:3 4 5 6
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}
Symmetric Difference: {1, 2, 5, 6}
