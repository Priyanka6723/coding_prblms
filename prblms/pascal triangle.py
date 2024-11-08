l=int(input())
def fact(x):
    if x==0 or x==1:
        return 1
    else:
        a=x*fact(x-1)
        return a
for n in range(l):
    print(' '*(l-n),end='')
    for r in range(n+1):
        print(fact(n)//(fact(r)*fact(n-r)),end=' ')
    print()


'''
input: 6
      1 
     1 1 
    1 2 1 
   1 3 3 1 
  1 4 6 4 1 
 1 5 10 10 5 1
 '''