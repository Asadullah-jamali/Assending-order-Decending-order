# for assending and decending order
n=[];m=[];o=[];p=[]
a = int(input("Enter the number of element in list 1: "))
b = int(input("Enter the number of element in list 2: "))
print('Enter data in list 1:')
for i in range(a):
    x=int(input())
    n.append(x)
print(n)
print('Enter data in lpist 1:')
for i in range(b):
    x=int(input())
    m.append(x)
print(m)
# marge two lists
for g in range(a):
    c=n[g]
    o.append(c)
for e in range(b):
    d=m[e]
    o.append(d)
print(o)
# for decending order
d=-1*(a+b)
for x in range(-1,d-1,-1):
    l=o[x]
    p.append(l)
print(p)    
