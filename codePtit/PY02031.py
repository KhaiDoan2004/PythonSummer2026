# Kiểm tra nguyên tố

import math
def check_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    else:
        return True
if __name__ == "__main__":
    n, m = map(int,input().split())
    matrix = []
    for i in range(n):
        hang = list(map(int,input().split()))
        matrix.append(hang)
    for i in range(n):
        for j in range(m):
            if check_so_nguyen_to(matrix[i][j]):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    for hang in matrix:
        print(*hang)
