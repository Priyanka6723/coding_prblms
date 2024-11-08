m = int(input())
n = int(input())
x = []
for i in range(m):
    r = list(map(int, input().split(' ')))
    x.append(r)
for i in range(m):  
    for j in range(i, n - i):
        print(x[i][j], end=' ')
    if i<n-i-1:
            a=i+1
            while(a<m-i):
                print(x[a][n-i-1],end=' ')
                a+=1
    if m - i - 1 > i:
        for j in range(n - i - 2, i - 1, -1):
            print(x[m - i - 1][j], end=' ')
    if n - i - 1 > i:
        for j in range(m - i - 2, i, -1):
            print(x[j][i], end=' ')