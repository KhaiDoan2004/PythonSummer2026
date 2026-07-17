# Tổng chữ số thuận nghịch 
def checksothuangnghich(n):
    s = str(n)
    if len(s) < 2:
        return False
    if s != s[::-1]:
        return False
    else:
        return True
t = int(input())
for _ in range (t):
    n = input()
    c = []
    for i in n:
        so = int (i)
        c.append(so)
    if checksothuangnghich(sum(c)):
        print("YES")
    else:
        print("NO")
