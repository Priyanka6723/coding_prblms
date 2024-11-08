def anagram(n,s):
    n=[i for i in n]
    n.sort()
    s=[i for i in s]
    s.sort()
    if n==s:
        return 'yes, it is anagram'
    else:
        return 'no, it is not anagram'
n=input()
s=input()
print(anagram(n,s))