# Bài 1: Đếm số lần xuất hiện của từng phần tử trong danh sách

# Nhập danh sách từ bàn phím (vd: 1 2 2 3 1 4)
a = list(map(int, input("Nhập danh sách: ").split()))

dem = {}
for x in a:
    if x in dem:
        dem[x] += 1
    else:
        dem[x] = 1

print(dem)
