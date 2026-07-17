# Liệt kê số đẹp 

def checksodep(n):
    s = str(n)
    le = [1,3,5,7,9]
    if(len(s) % 2 != 0):
        return False
    if s != s[::-1]:
        return False
    for i in range(len(s)):
        so = int(s[i])
        if so in le:
            return False
    else: 
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    z = 22 
    while z < n:
        if checksodep(z):
            print(z, end=' ')
        z = z + 2
    print()
