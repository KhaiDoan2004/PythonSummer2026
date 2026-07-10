
a = [10, "Python", 20.5, "Ngựa", 30]

c = 0
t = 0
for i in a:
    if type(i) in(int, float):
        c = c + 1
        t = t + i
if c > 0:
    print(t, t /c)