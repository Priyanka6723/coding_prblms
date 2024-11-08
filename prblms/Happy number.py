def rec(n):
    b=0
    while(n):
        a=n%10
        b=b+a**2
        n=n//10
    return b
def happynum(n):
    while n>9:
        n=rec(n)
    if n==1:
        return 'It is happy number'
    else:
        return 'It is not a happy number'
 
n=int(input())
print(happynum(n))