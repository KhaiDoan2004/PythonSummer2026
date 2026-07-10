# Ngưỡng tối thiểu 

s = input()
k = int(input())
a = []
for i in range (0, len(s),2):
    so = s[i: i+2]
    a.append(so)
b = list(dict.fromkeys(a))
b.sort()
find = False
for i in b:
    c = 0
    for j in a:
        if i == j:
            c = c + 1
    if c >= k:
        find = True
        print(i,c)
            
if find == False:
    print("NOT FOUND")       


