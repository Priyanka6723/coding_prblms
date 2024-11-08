m=int(input())
n=int(input())
x=[]
for i in range(m):
    r=list(map(int,input().split(' ')))
    x.append(r)
for i in range(len(x)):
    if i%2==0:
        print(*x[i],end=' ')
    else:
        a=x[i]
        print(*a[::-1],end=' ')







        