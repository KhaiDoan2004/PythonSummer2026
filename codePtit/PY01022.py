n = input()

if n[0] == '-':
    b = n[1:]
    a = int(b)
else:
    a =int(n)
tong = 0
dem = 0
while a > 9:
    for i in range(len(n)):
        tong = tong + int(n[i])
        tong = a
        dem = dem + 1

print(dem)



