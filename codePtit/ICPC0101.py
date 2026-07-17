# Thu gọn dãy số 

n = int(input())
a = list(map(int,input().split()))
b = []
for i in range (len(a)):
    if len(b) > 0 and (a[i] + b[-1]) % 2 == 0:
        b.pop()
    else:
        b.append(a[i])
print(len(b))
