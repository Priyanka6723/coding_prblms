n=list(map(int,input().split(' ')))
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            a=n[i]
            n[i]=n[j]
            n[j]=a
print(n)
     