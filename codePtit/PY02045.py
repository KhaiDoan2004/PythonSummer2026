n = int(input())
y = str(n)
i = 0
c = 0
while len(y)>1:
    e = y[i:len(y)//2]
    z = y[len(y)//2:]
    so1= int(e)
    so2= int(z)
    c = so1 + so2
    print(c)
    y = str(c)

