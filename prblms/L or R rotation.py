def rotate(s,r,n):
    if r=='l':
        return s[n:]+s[:n]
    else:
        return s[-n:]+s[:-n]

s=input()
r=input()
n=int(input())
print(rotate(s,r,n))


'''
input:
zohocorporation
r
5 

right rotation output:
ationzohocorpor

left ratation output:
orporationzohoc
'''