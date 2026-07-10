# Bài 4: Vẽ hình chữ nhật rỗng

n, m = map(int, input("Nhập số hàng n và số cột m: ").split())

for i in range(n):
    for j in range(m):
        # Nếu là hàng đầu, hàng cuối, cột đầu hoặc cột cuối -> In sao
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print("*", end="")
        else:
            print(" ", end="")
    # Hết 1 hàng thì xuống dòng
    print()