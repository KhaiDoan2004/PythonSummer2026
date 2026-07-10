# Bài 5: Vẽ tam giác vuông cân rỗng

n = int(input("Nhập độ dài cạnh góc vuông n: "))

for i in range(n):
    for j in range(i + 1):
        # Nếu là cột đầu tiên, hàng cuối cùng, hoặc phần tử nằm trên đường chéo -> In sao
        if j == 0 or i == n - 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
