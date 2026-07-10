# PHAO CỨU SINH - Cú Pháp Python Hay Quên
*(Copy-paste ngay khi cần, khỏi phải nhớ)*

---

## 1. NHẬP DỮ LIỆU (Input)

### Nhập 1 số nguyên
```python
n = int(input())
```

### Nhập 2 số trên cùng 1 dòng (cách nhau bởi dấu cách)
```python
n, m = map(int, input().split())
```

### Nhập mảng số nguyên trên 1 dòng
```python
a = list(map(int, input().split()))
```

### Nhập ma trận (mảng 2 chiều) gồm n hàng
```python
matrix = []
for _ in range(n):
    hang = list(map(int, input().split()))
    matrix.append(hang)
```

### Nhập chuỗi (string)
```python
s = input()
```

---

## 2. XUẤT DỮ LIỆU (Output / Print)

### In mảng trên 1 dòng, cách nhau bởi dấu cách
```python
print(*a)                     # In: 1 2 3 4 5
```

### In nhiều thứ trên 1 dòng (tự động cách 1 space)
```python
print("Hello", s)             # In: Hello Nam
```

### In nhiều thứ KHÔNG cách space
```python
print("Hello", s, sep="")     # In: HelloNam
```

### In mà KHÔNG xuống dòng
```python
print(x, end=" ")             # In xong thêm 1 space thay vì xuống dòng
print(x, end="")              # In xong không thêm gì cả
```

### In từng hàng của ma trận
```python
for hang in matrix:
    print(*hang)
```

---

## 3. SẮP XẾP (Sort)

### Sắp xếp tăng dần (mặc định)
```python
a.sort()                      # Sắp xếp trực tiếp trên mảng a
b = sorted(a)                 # Tạo mảng mới b đã sắp xếp, a giữ nguyên
```

### Sắp xếp giảm dần
```python
a.sort(reverse=True)
b = sorted(a, reverse=True)
```

---

## 4. LỌC TRÙNG

### Lọc trùng (MẤT thứ tự) - dùng `set()`
```python
b = list(set(a))
```

### Lọc trùng (GIỮ thứ tự) - dùng `dict.fromkeys()`
```python
b = list(dict.fromkeys(a))
```

### Lọc trùng thủ công (GIỮ thứ tự) - dùng vòng lặp
```python
b = []
for i in a:
    if i not in b:
        b.append(i)
```

---

## 5. ĐẾM SỐ LƯỢNG (Count)

### Đếm 1 phần tử xuất hiện bao nhiêu lần trong mảng
```python
so_lan = a.count(3)           # Đếm số 3 xuất hiện bao nhiêu lần trong a
```

### Đếm 1 ký tự trong chuỗi
```python
so_lan = s.count('C')         # Đếm chữ C trong chuỗi s
```

### Đếm tất cả phần tử bằng Counter
```python
from collections import Counter
dem = Counter(a)              # dem = {1: 2, 3: 4, 5: 1}
dem[3]                        # Lấy số lần xuất hiện của số 3
dem.keys()                    # Lấy danh sách các phần tử
dem.values()                  # Lấy danh sách số lần xuất hiện
```

---

## 6. CẮT CHUỖI (Slicing)

### Cắt chuỗi con
```python
s = "ABCDEF"
s[0:2]                        # "AB" (từ index 0 đến 1)
s[2:5]                        # "CDE" (từ index 2 đến 4)
s[:3]                         # "ABC" (từ đầu đến index 2)
s[3:]                         # "DEF" (từ index 3 đến hết)
```

### Cắt chuỗi từng cặp 2 ký tự (bước nhảy 2)
```python
s = "123456"
for i in range(0, len(s) - 1, 2):
    cap = s[i : i+2]          # "12", "34", "56"
```

---

## 7. VÒNG LẶP (Loop)

### range() cơ bản
```python
range(5)                      # 0, 1, 2, 3, 4
range(2, 7)                   # 2, 3, 4, 5, 6
range(0, 10, 2)               # 0, 2, 4, 6, 8 (bước nhảy 2)
range(10, 0, -1)              # 10, 9, 8, ..., 1 (đếm ngược)
```

### Duyệt mảng bằng index
```python
for i in range(len(a)):
    print(a[i])
```

### Duyệt mảng bằng phần tử
```python
for x in a:
    print(x)
```

---

## 8. HÀM TOÁN HỌC HAY DÙNG

### Căn bậc 2 (số nguyên) - dùng cho kiểm tra nguyên tố
```python
import math
math.isqrt(25)                # 5 (căn bậc 2 nguyên)
```

### Ước chung lớn nhất (GCD)
```python
import math
math.gcd(12, 8)               # 4
```

### Tổ hợp chập k của n
```python
import math
math.comb(5, 2)               # 10 (C(5,2) = 10)
```

### Tổng mảng
```python
sum(a)                        # Tổng tất cả phần tử trong mảng a
```

### Giá trị lớn nhất / nhỏ nhất
```python
max(a)                        # Phần tử lớn nhất
min(a)                        # Phần tử nhỏ nhất
```

### Độ dài mảng / chuỗi
```python
len(a)                        # Số phần tử trong mảng
len(s)                        # Số ký tự trong chuỗi
```

---

## 9. ÉP KIỂU (Type Casting)

```python
int("123")                    # Chuỗi -> Số nguyên: 123
str(123)                      # Số -> Chuỗi: "123"
float("3.14")                 # Chuỗi -> Số thực: 3.14
list("abc")                   # Chuỗi -> Mảng: ['a', 'b', 'c']
```

---

## 10. MẸO VẶT KHÁC

### Hoán đổi 2 biến (Swap)
```python
a, b = b, a
```

### Kiểm tra phần tử có trong mảng không
```python
if x in a:
if x not in a:
```

### Biến cờ (Flag) - xử lý "NOT FOUND"
```python
find = False
for ...:
    if điều_kiện:
        find = True
        print(kết_quả)
        break

if not find:
    print("NOT FOUND")
```

---
*Ghi chú: File này sẽ liên tục được cập nhật khi Chủ nhân học thêm cú pháp mới!*
