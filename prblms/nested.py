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

#input: n=10 2 3 4 5 6 7 8,   tar=23
#output:
'''
10 2 3 8
10 2 4 7
10 2 5 6
10 3 4 6
10 6 7
2 6 7 8
3 5 7 8
4 5 6 8'''