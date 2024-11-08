n=input()
d={}
l=[]
for i in range(len(n)):
    if n[i] not in d or n[i]==n[i-1]:
        d[n[i]]=i
    else:
        d[n[i]]=i-d[n[i]]
        l.append(d[n[i]])
print(max(l)-1)

'''
input: abcbda
output: 4

input: abacdeefghdei
output: 5 '''