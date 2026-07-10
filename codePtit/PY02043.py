s = input()
n = int(input())
d = str(n)
c = 0
i = 0
while i <len(s) - len(d):
    e = s[i: i +len(d)]
    so = int(e)
    if so == n :
        i = i + len(d)
        c = c + 1
    else:
        i = i + 1
print(c)



