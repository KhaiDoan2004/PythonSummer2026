def checksothuannghich(n):
    o_n = n
    if o_n < 10: 
        return False
    tmp = 0 
    r = 0
    while n > 0: 
        tmp = n % 10
        r = r * 10 + tmp
        n = n // 10
    if r == o_n:
        return True

if checksothuannghich(1221):
    print("OK")
else:
    print( "KAKAKA")