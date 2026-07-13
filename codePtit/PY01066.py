# Xâu ký tự thăng bằng 
n = int(input())
for i in range(n):
    s = input()
    y = []
    check = True
    for i in range(len(s)-1, -1, -1):
        y.append(s[i])
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1])) != abs(ord(y[i])-ord(y[i+1])):
            check = False
            break
    if check :
        print("YES")
    else:
        print("NO")
            