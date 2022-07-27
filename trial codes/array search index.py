from array import *
x= int(input("enter the length of the array"))
first= array('i',[])
for i in range(x):
    y= int(input("enter the number"))
    first.append(y)
print (first)
z=  int(input(" enter value to be searched"))
d=0
for j in first:
    if j==z:
        print(d)
        break
    d=d+1
print("bye")
