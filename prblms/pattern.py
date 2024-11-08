n=int(input())
a=1
for i in range(n):
    print(' '*(n-i),end='')
    for j in str(a):
        print(j,end=" ")
    print()
    a=a*11
#for i in range(n):
#    print(11**i)
