x = int(input("enter your number."))
y= int(x/2)
for i in range(2,y):
    if x % i == 0:
        print ("not prime")
        break
else:
    print("prime")