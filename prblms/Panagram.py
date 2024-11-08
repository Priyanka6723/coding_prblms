def isPanagram(S):
    s=[]
    x='abcdefghijklmnopqrstuvwxyz'
    for j in S:
    	j=j.lower()
        if j in x:
		    s.append(j)
            
    s=set(s)
    for i in x: 
	    if i not in s:
	        return 0
    else:
	    return 1
		
S=input()
print(isPanagram(S))
		
        