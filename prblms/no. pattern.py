n=int(input())
a=1
for i in range(1,n+1):
    print(' '*(n-i), end='')
    for j in range(i):
        print(a,end=' ')
        a+=1
    print() 
for i in range(n+1,1,-1):
    print(' '*(n-i+1), end='')
    for j in range(i-1):
        a-=1
        print(a,end=' ')
    print() 


'''
input: 4
   1
  2 3
 4 5 6
7 8 9 10
10 9 8 7
 6 5 4
  3 2
   1
'''