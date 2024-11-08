n=list(map(int,input().split(' ')))
tar=int(input())
c=[]
def fun():
    if l not in c:
        c.append(l)
        print(*l)
    else:
        pass
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        for k in range(j+1,len(n)):
            for x in range(k+1,len(n)):
                if (n[i]+n[j])==tar:
                    l=[n[i],n[j]]
                    fun()
                if n[i]+n[j]+n[k]==tar:
                    l=n[i],n[j],n[k]
                    fun()
                if n[i]+n[j]+n[k]+n[x]==tar:
                    l=n[i],n[j],n[k],n[x]
                    fun()