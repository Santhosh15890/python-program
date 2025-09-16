l=[]
n=int(input("Enter a number of element"))
for i in range(0,n):
    m=int(input("Enter a element"))
    l.append(m)
print(l)
print(l[0:3])
print(l[2:5])
print(l[-4:-1])
print(l[-4:])
print(l[-3:])
l.extend([6,7,8])
print(l)
