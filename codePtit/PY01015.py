# số không giảm 
t = int(input())
for _ in range(t):
    n = input()
    a = []
    for i in n:
        so =int(i)
        a.append(so)
        check = True
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            check = False
            break
        else:
            check =True
    if check:
        print("YES")
    else:
        print("NO")