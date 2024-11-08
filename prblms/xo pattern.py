m=int(input())
n=int(input())
x=[]
for i in range(m):
    r=[]
    for j in range(n):
        if (i==0 or i==m-1) or (j==0 or j==n-1): 
            r.append('X')
        else:
            if (m//2==n//2) and(i==m//2)and (j==n//2) and (m%2!=0 and n%2!=0):
                r.append('X')
            else:
                r.append('0')
    x.append(r)
for i in x:
    print(' '.join(i))  