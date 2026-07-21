# Chữ hoa - chữ thường 
s = input()
c = 0
for i in range(len(s)):
    if s[i].isupper():
        c = c + 1
if c > len(s)- c:
    d = s.upper()
    print(d)
else:
    d = s.lower()
    print(d)