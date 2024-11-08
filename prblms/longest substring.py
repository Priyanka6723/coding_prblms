#longest substring without repeated characters
n=input()
s=''
for i in range(len(n)):
    if n[i] in s:
        s=''  
    else:
        s=s+n[i]
print(s)