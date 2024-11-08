n=input()
for i in range(len(n)):
    if i<(len(n)//2):
        print(' '*(i+1),n[i],end='')
        print(' '*(len(n)-i*2-1),end='')
        print(n[i])
    if i==len(n)//2:
        print(' '*(i+2), end='')
        print(n[i])
    if i>len(n)//2:
        print(' '*(len(n)-i),n[i],end='')
        print(' '*(i*2-len(n)),end=' ')
        print(n[i])