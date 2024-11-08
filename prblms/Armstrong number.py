def rem(n):
    a=n%10
    l.append(a)
    if n>10:
        n=n-a
        rem(n//10)
def sum(n):
    rem(n)
    s=0
    for i in l:
        s=s+i**3
    if n==s or n<10:
        return 'yes it is armstrong number'
    return 'No it is not armstrong number'

l=[]
n=int(input())
print(sum(n))