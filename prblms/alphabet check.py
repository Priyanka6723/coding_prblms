k =input()
a='abcdefghijklmnopqrstuvwxyz'
k=set(k.lower())
if len(k)<len(a):
    print('false')
else:
    for i in a:
        if i not in k:
            print('false')
            break
    else:
        print('true')