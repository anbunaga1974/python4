n=int(input("Enter no. of items:"))
def getinput(n):
   l=[]
   for i in range(n):
      print(f"\nEnter details of item{i+1}:")
      i_name=input("Enter item name:")
      quantity=int(input("Enter Quantity:"))
      price=int(input("Enter price:"))
      l.append((i_name,quantity,price))
   return l
def subtotal(l):
   s=[]
   for i in range(len(l)):
      sub=l[i][1]*l[i][2]
      s.append(sub)
   return s
def total(l):
   t=0
   for i in range(len(s)):
      t=t+s[i]
   print("Total:",t)
   if t>3000:
      d=t*(10/100)
      t=t-d
      print("After discount:",t)
   else:
      d=0
      t=t-d
      print("After discount:",t)
   g=t*(5/100)
   t=g+t
   print("GST:",g)
   print("Final Amount:",t)
r=getinput(n)
print("Items:",r)
s=subtotal(r)
print("Subtotal:",s)
total(s)
