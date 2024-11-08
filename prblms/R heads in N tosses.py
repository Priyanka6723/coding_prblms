def fact(x):
    if x==0 or x==1:
        return 1
    else:
        a=x*fact(x-1)
        return a
def prob(n,r):
    out= fact(n)/fact(r)*fact(n-r)
    out=out/2**n
    return f"{out:.6f}"

n=int(input())
r=int(input())
print(prob(n,r))