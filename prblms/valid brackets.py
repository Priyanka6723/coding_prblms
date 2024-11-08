def valid_brackets(n):
    open='{[('
    close='}])'
    stack=[]
    for i in n:
        if i in open:
            stack.append(i)
        elif i not in close:
            pass
        else:
            if len(stack)!=0 and ((stack[-1]=='{' and i=='}') or (stack[-1]=='[' and i==']') or (stack[-1]=='(' and i==')')):
                stack.pop()
            else:
                return False
    return not stack
n=input()
print(valid_brackets(n))