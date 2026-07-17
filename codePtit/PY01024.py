# Chẵn - lẻ

t = int(input())
for _ in range (t):
    n  = input()
    a = [int(i) for i in n]
    check = True
    if sum(a) % 10 != 0:
        check = False
    else:
        for i in range(len(a)-1):
            if abs(a[i] - a[i+1]) != 2:
                check = False
                break
            else:
                check = True
    if check:
        print("YES")
    else:
        print("NO")
        