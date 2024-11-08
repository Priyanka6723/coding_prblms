n=input()
m=input()
l=[]
for i in m:
    for j in range(len(n)):
        if n[j]==i:
            l.append(j)
            break
l.sort()
print(n[l[0]:l[-1]+1])