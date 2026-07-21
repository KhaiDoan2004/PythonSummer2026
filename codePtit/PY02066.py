 # Bài toán đếm 

n = int(input())
a = list(map(int,input().split()))
while len(a) < n:
    a.extend(map(int,input().split()))
b = []
for i in range(1, a[-1]+1):
    if i not in a:
        b.append(i)
if len(b) < 1:
    print("Excellent!")
else:
    for i in b:
        print(i)
