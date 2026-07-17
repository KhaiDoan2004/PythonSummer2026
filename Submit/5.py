if __name__ == '__main__':
    try:
        n = int(input("Nhập cạnh góc vuông n: "))
        for i in range(n):
            for j in range(i + 1):
                if j == 0 or j == i or i == n - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    except ValueError:
        print("Vui lòng nhập số nguyên.")
