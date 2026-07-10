# PY02038 - Đếm cặp đồng xu
# Yêu cầu: Luyện tập vét cạn (Logic C++)
# Cấm dùng công thức Toán Tổ Hợp, bắt buộc dùng 3 vòng lặp lồng nhau để luyện cơ bắp.

n = int(input())
matrix = []
for i in range(n):
    hang = input()
    matrix.append(hang)

tong = 0

# BƯỚC 1: VÉT CẠN HÀNG NGANG
# Gợi ý: 
# for i in range(n):           # Chốt hàng i
#     for j in range(n):       # Ô thứ nhất
#         for k in range(j+1, n):  # Ô thứ hai đứng sau ô thứ nhất
#             Nếu cả 2 ô đều là 'C' thì tăng tong lên 1.

# NGÀI CODE BƯỚC 1 VÀO ĐÂY:



# BƯỚC 2: VÉT CẠN CỘT DỌC
# Gợi ý:
# Đảo vòng lặp! Khóa chặt cột j ra vòng ngoài cùng.
# 2 vòng lặp trong (i và k) dùng để duyệt dọc xuống dưới.
# Cẩn thận nhét biến i, j, k vào dấu ngoặc vuông cho đúng vị trí!

# NGÀI CODE BƯỚC 2 VÀO ĐÂY:



print(tong)
