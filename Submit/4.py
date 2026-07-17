if __name__ == '__main__':
    try:
        n = int(input("Nhập số hàng n: "))
        m = int(input("Nhập số cột m: "))
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    except ValueError:
        print("Vui lòng nhập số nguyên.")
