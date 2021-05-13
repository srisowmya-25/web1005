num=int(input())
temp=num
c=r=f=l=nn=k=0
p=1
while num:
    r=num%10
    num=num//10
    c+=1
num=temp
k=c=c-1
print(k)
if num>0:
    l=num%10
    f=num//pow(10,c)
while num:
    r=num%10
    num=num//10
    if c==k:
        r=f
    elif c==0:
        r=1
    nn=nn+r*p
    p=p*10
    c-=1
print(nn)
    
