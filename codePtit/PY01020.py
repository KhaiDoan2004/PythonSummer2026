# Số Phát lộc 
t = int(input())
for _ in range(t):
    n = input()
    if len(n) > 2 and n[-2:] == "86":
        print("YES")
    else:
        print("NO")