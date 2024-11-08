#Minimum Operations to Make Array Equal to Target array
def min_oper(a,b):
    count=0
    for i in range(len(a)):
        if a[i]==b[i]:
            pass
        if a[i]<b[i]:
            while a[i]<b[i]:
                a[i]=a[i]+1
                count=count+1
        elif a[i]>b[i]:
            while a[i]>b[i]:
                a[i]=a[i]-1
                count=count+1
    return count

a=list(map(int, input().split(',')))
b=list(map(int, input().split(',')))
if len(a)==len(b):
    print(min_oper(a,b))
else:
    print(False)