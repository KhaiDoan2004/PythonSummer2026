t = int(input())
for _ in range(t):
    a = input()
    c = []
    b = input()
    d = []
    check = True
    for i in a:
        if i not in c:
            c.append(i)
    c.sort()        
    for i in b:
        if i not in d:
            d.append(i)
    d.sort()        
    if len(c) != len(d) or len(a) != len(b):
        check = False
    else:
        for i in range(len(c)):
            if a.count(c[i]) != b.count(d[i]) or ord(c[i]) != ord(d[i]) :
                check = False
                break
            else:
                check = True
    if check == False:
        print(f"Test {_ + 1}: NO")
    else:
        print(f"Test {_ + 1}: YES")

