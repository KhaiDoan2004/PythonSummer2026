# Số xen kẽ 
n = int(input())
for i in range(n):
    a = int(input())
    s = str(a)
    y = []
    check = True
    for i in range(len(s)):
        so = int (s[i])
        y.append(so)
    if len(y) % 2 == 0 or s[0] == s[1]:
        check = False
        for i in range(0, len(y) - 2, 2):
            if s[i] != s[i+2]:
                check = False
                break
    if check == True:
        print("YES")
    else:
        print("NO")