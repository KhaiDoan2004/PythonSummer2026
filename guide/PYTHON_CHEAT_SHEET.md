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

### Đếm 1 ký tự / xâu con trong chuỗi (KHÔNG trùm lên nhau)
```python
s = "121212"
s.count('1')                  # Đếm số chữ '1' xuất hiện
s.count("121")                # Trả về 1 (vì tìm thấy "121" ở đầu, đoạn sau còn "212" không khớp)
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

## 11. ĐIỀU KHIỂN LUỒNG & LOGIC

### Lệnh `continue` (Bỏ qua sớm / Early Exit)
Giúp chương trình bỏ qua vòng lặp hiện tại ngay khi phát hiện lỗi, thay vì lồng nhiều khối `if/else`.
```python
for x in range(5):
    if x % 2 == 0:
        continue  # Gặp số chẵn thì bỏ qua luôn, vòng ngược lên
    print("Số lẻ:", x)
```

### Tư duy cờ (Flag) đúng chuẩn
Khi cần kiểm tra một tính chất mà "tất cả các phần tử phải thỏa mãn điều kiện", hãy luôn đặt niềm tin (`True`) từ đầu. Khi gặp lỗi thì gán `False` và `break`. Đừng làm ngược lại!
```python
# Sai: Không gán True bao giờ
check = False 
for x in a:
    if x % 2 == 0: check = False

# Đúng chuẩn:
check = True  # Luôn tin tưởng
for x in a:
    if x % 2 != 0: 
        check = False  # Bắt quả tang sai
        break          # Phạt rút thẻ đỏ luôn
```

---

## 12. ASCII VÀ KHOẢNG CÁCH KÝ TỰ (ord, abs)

### Lấy mã thứ tự ASCII của 1 ký tự
```python
ord('a')                      # 97
ord('c')                      # 99
```

### Tính khoảng cách giữa 2 ký tự (Trị tuyệt đối)
Dùng kết hợp `abs()` (Absolute) và `ord()`.
```python
kc = abs(ord('a') - ord('c')) # |97 - 99| = 2
```

---

## 13. TUYỆT KỸ ĐẢO NGƯỢC (Đảo chuỗi / Đảo mảng)

### Cách Pythonic nhất: Dùng Slicing `[::-1]`
Đây là "trick" ngắn nhất vũ trụ của Python, áp dụng được cho cả Chuỗi (String) và Mảng (List).
```python
# Đảo chuỗi
s = "abcde"
s_dao = s[::-1]               # "edcba"

# Đảo mảng
a = [1, 2, 3, 4]
a_dao = a[::-1]               # [4, 3, 2, 1]
```

### Đảo ngay tại chỗ (chỉ dành cho Mảng)
```python
a = [1, 2, 3]
a.reverse()                   # Mảng a bị biến đổi thẳng thành [3, 2, 1]
```

### Hàm `reversed()` (Dành cho duyệt vòng lặp)
```python
s = "abc"
for char in reversed(s):
    print(char)               # In ra: c, b, a
```

---

## 14. BẢN CHẤT BỘ NHỚ: C++ vs PYTHON (Name Tag)

### C++ (Cái Hộp)
Trong C++, biến là một **cái hộp cố định** trong RAM. Khi khai báo `int a`, máy cắt sẵn một cái hộp dung lượng 4 bytes. Nếu nhét dữ liệu lớn hơn vào (ví dụ chuỗi 1000 chữ số), hộp sẽ vỡ tung (Tràn bộ nhớ - Overflow). Khi cập nhật biến, máy phải bới cái hộp đó lên, đổ dữ liệu cũ ra và nhét dữ liệu mới vào.

### Python (Nhãn Dán)
Trong Python, biến chỉ là một **"Cái Nhãn Dán" (Name Tag)**.
- Khi gán `y = "123"`, Python đúc ra cục dữ liệu `"123"` ở đâu đó trong RAM, rồi dán nhãn `y` lên.
- Khi cập nhật `y = "456"`, Python đúc ra cục dữ liệu `"456"` mới tinh ở một nơi khác, bóc nhãn `y` ở chỗ cũ dán sang chỗ mới.
- Cục `"123"` cũ bị bỏ rơi sẽ bị "Người thu gom rác" (Garbage Collector) của Python tự động hốt đi tiêu hủy để dọn dẹp RAM.
👉 Do đó, việc tái sử dụng biến, cập nhật biến, ép kiểu biến (từ `string` sang `int` rồi lại sang `string`) cực kỳ an toàn và không bao giờ rác bộ nhớ!

---

## 15. BẪY VÒNG LẶP FOR (Python vs C++)

### Trong C++ (Cộng dồn)
`for (int i = 0; i < n; i++)` hoạt động dựa trên việc **cộng dồn**. Nếu bên trong vòng lặp ta tự ý cập nhật `i = i + 3`, vòng lặp vẫn tôn trọng giá trị đó và chạy tiếp từ `i` mới. Tính năng "nhảy cóc" này rất tiện.

### Trong Python (Băng chuyền)
`for i in range(10)` hoạt động như một **băng chuyền**. `range(10)` đã sản xuất sẵn 10 viên bi từ `0` đến `9`.
Cứ mỗi lần chạy lại vòng mới, cái máy `for` sẽ bốc viên bi tiếp theo từ băng chuyền và **tự động gán đè lên biến `i`**. 
Mọi nỗ lực cập nhật `i = i + 3` của ngài ở vòng trước đều bị cái máy `for` này tàn nhẫn ghi đè mất!

👉 **Giải pháp:** Nếu muốn tự tay cập nhật biến đếm (bước nhảy không đều), HÃY DÙNG VÒNG LẶP `while`:
```python
i = 0
while i < len(s):
    if điều_kiện_khớp:
        i += 3  # Nhảy cóc 3 ô thoải mái!
    else:
        i += 1  # Nhích 1 ô
```

---

## 16. KỸ THUẬT HAI CON TRỎ (Two Pointers) & XẢ BỘ ĐỆM (Buffer Flush)

Đây là tuyệt kỹ cực kỳ phổ biến để xử lý mảng/chuỗi. Biến thể **Neo và Quét (Anchor & Scan)** giúp ta bóc tách các nhóm dữ liệu rời rạc dựa trên một điều kiện "đứt gãy".

### Cấu trúc cơ bản
- **Mỏ Neo (`start`)**: Đứng im ở vị trí đầu của nhóm hiện tại.
- **Tia Quét (`i`)**: Chạy vòng `for` thăm dò phía trước. Khi gặp vạch đứt gãy, nó ra lệnh "Cắt", sau đó lập tức rút Mỏ Neo cắm sang vị trí mới.

### Bắt buộc: Xả Bộ Đệm (Buffer Flush)
Vì nhát cắt chỉ xảy ra ở *BÊN TRONG* mảng, phần đuôi mảng cuối cùng sẽ bị "kẹt" lại (vì không còn nhát cắt nào phía sau để xả nó ra). Ta luôn phải có một lệnh vét đáy nằm **BÊN NGOÀI** vòng lặp.

### Ví dụ Code:
```python
a = [1, 2, 3, 4, 6, 7, 9]
k = 1
start = 0

for i in range(len(a) - 1):
    # Dấu hiệu đứt gãy
    if a[i+1] - a[i] > k:
        nhom = a[start : i+1]      # Cắt nhóm
        print(nhom)
        start = i + 1              # Nhổ mỏ neo cắm sang vị trí mới

# Lệnh Buffer Flush (Luôn phải có để vét nốt khúc cuối)
print(a[start : len(a)]) 
```

---

## 17. ĐỊNH DẠNG CHUỖI SIÊU TỐC (F-String)

F-String là "ma thuật" in chuỗi thanh lịch nhất của Python, dẹp bỏ mọi dấu phẩy và phép cộng chuỗi rườm rà.
Chỉ cần đặt chữ `f` trước dấu ngoặc kép, và bọc biến vào trong `{ }`.

```python
i = 2
j = 1
# In ra: Vi tri [2][1]
print(f"Vi tri [{i}][{j}]")

ten = "Lữ Bố"
vu_khi = "Phương Thiên Họa Kích"
print(f"Tướng quân {ten} vung {vu_khi} ra trận!")
```

---

## 18. NHỮNG CÁI BẪY CHẾT NGƯỜI VÀ MẸO NHỎ

### Bẫy hàm `range()` thiếu 1 bước
Hàm `range(start, end)` luôn luôn **dừng lại ở `end - 1`**. 
Lỗi kinh điển nhất là vòng lặp kiểm tra số nguyên tố:
```python
# SAI: Căn bậc 2 của 9 là 3. range(2, 3) chỉ chạy đến 2 rồi dừng. 9 bị kết luận là số nguyên tố!
for i in range(2, math.isqrt(n)):

# ĐÚNG: Phải cộng thêm 1 để vòng lặp chạm tới được phần nguyên của căn bậc 2.
for i in range(2, math.isqrt(n) + 1):
```

### Sử dụng `-1` làm Cờ hiệu (Sentinel Value)
Khi tìm kiếm một vị trí (index) hoặc một giá trị dương (ví dụ tìm số Max, tìm số nguyên tố), người ta thường khởi tạo biến lưu trữ bằng `-1`. 
Số `-1` đóng vai trò là Cờ hiệu báo rằng "Tôi chưa tìm thấy gì cả".
Đến cuối chương trình, nếu biến đó vẫn là `-1`, ta kết luận `NOT FOUND`.

```python
max_prime = -1
for x in a:
    if x > max_prime and checksonguyento(x):
        max_prime = x

if max_prime == -1:
    print("NOT FOUND")
else:
    print(max_prime)
```

---
*Ghi chú: File này sẽ liên tục được cập nhật khi Chủ nhân học thêm cú pháp mới!*
