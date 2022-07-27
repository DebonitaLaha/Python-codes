list=[]
for i in range (6):
    values = int(input())
    list.append(values)
print(list)
list.sort()
print(list)
print("seconf largest",list[len(list)-2],end="")
for j in range(5):
    if list[j]==list[j-1]:
        print(list[j],end="")

print("bye")


