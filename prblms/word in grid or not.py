# Check if a word exists in a grid or not
def check_word(mat,tar,m,n,row,col):
    ch=[]
    i,j=m,n
    for k in range(1,len(tar)):
        l=[[i-1,j],[i-1,j-1],[i,j-1],[i+1,j-1],[i+1,j],[i+1,j+1],[i,j+1],[i-1,j+1]]
        for a,b in l:
            if (0>=a or a<=row-1) and (0>=b or b<=col-1):
                if (mat[a][b]==tar[k-1]) and (tar[k]==tar[k-1]):
                    pass
                elif mat[a][b]==tar[k]:
                    i=a
                    j=b
                    ch.append(tar[k])
    if len(ch)==(len(tar)-1):
        return True
    else:
        return False
    
def check_grid(mat,tar,row,col):
    for i in range(row):
        for j in range(col):
            if mat[i][j]==tar[0]:
                return check_word(mat,tar,i,j,row,col)
    else:
        return False

row=int(input())
col=int(input())
tar=input()
mat=[]
for i in range(row):
    val=list(input().split())
    mat.append(val)
print(check_grid(mat,tar,row,col))

'''
input:
4       
4
geeks
a x m y
b g d f
x e e t
r a k s

output:
True'''