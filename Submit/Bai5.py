a = [4, 1, 7, 3, 9]

b = []
for i in a:
    b.append(i * i)

b.sort(reverse=True)
print(b)
