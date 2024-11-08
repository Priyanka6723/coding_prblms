n=input()
tar=input()
for i in range(len(n)):
    if n[i:i+len(tar)]==tar:
        print(i)
else:
    print(-1)

