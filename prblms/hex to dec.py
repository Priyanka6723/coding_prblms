m=input() #'01B'
n=input() #'378'

a=int(m,16) #input contains characters i.e. '01B' -it will convert it to decimal value
b=hex(int(n,16)) #if i/p is full numbers as string then use this

print(a)
print(b[2:]) # b=0x378 --> b[2:]=378

sum=hex(int(m,16)+int(n,16))
print(sum[2:])