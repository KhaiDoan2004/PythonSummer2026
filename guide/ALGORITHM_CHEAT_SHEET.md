# PHAO CỨU SINH - Tư Duy Thuật Toán & Kỹ Thuật Lập Trình
*(Các mẫu thiết kế thuật toán và mẹo tư duy để giải quyết bài toán phức tạp)*

---

## 1. KỸ THUẬT HAI CON TRỎ (Two Pointers) & XẢ BỘ ĐỆM (Buffer Flush)

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

## 2. BẢN CHẤT BỘ NHỚ: C++ vs PYTHON (Name Tag)

### C++ (Cái Hộp)
Trong C++, biến là một **cái hộp cố định** trong RAM. Khi khai báo `int a`, máy cắt sẵn một cái hộp dung lượng 4 bytes. Nếu nhét dữ liệu lớn hơn vào (ví dụ chuỗi 1000 chữ số), hộp sẽ vỡ tung (Tràn bộ nhớ - Overflow). Khi cập nhật biến, máy phải bới cái hộp đó lên, đổ dữ liệu cũ ra và nhét dữ liệu mới vào.

### Python (Nhãn Dán)
Trong Python, biến chỉ là một **"Cái Nhãn Dán" (Name Tag)**.
- Khi gán `y = "123"`, Python đúc ra cục dữ liệu `"123"` ở đâu đó trong RAM, rồi dán nhãn `y` lên.
- Khi cập nhật `y = "456"`, Python đúc ra cục dữ liệu `"456"` mới tinh ở một nơi khác, bóc nhãn `y` ở chỗ cũ dán sang chỗ mới.
- Cục `"123"` cũ bị bỏ rơi sẽ bị "Người thu gom rác" (Garbage Collector) của Python tự động hốt đi tiêu hủy để dọn dẹp RAM.
👉 Do đó, việc tái sử dụng biến, cập nhật biến, ép kiểu biến (từ `string` sang `int` rồi lại sang `string`) cực kỳ an toàn và không bao giờ rác bộ nhớ!

---

## 3. BẪY VÒNG LẶP FOR (Python vs C++)

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

## 4. TƯ DUY CỜ HIỆU (Flag) & BỎ QUA SỚM (Early Exit)

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
# Đúng chuẩn:
check = True  # Luôn tin tưởng
for x in a:
    if x % 2 != 0: 
        check = False  # Bắt quả tang sai
        break          # Phạt rút thẻ đỏ luôn
```

### Sử dụng `-1` làm Cờ hiệu (Sentinel Value)
Khi tìm kiếm một vị trí (index) hoặc một giá trị dương (ví dụ tìm số Max, tìm số nguyên tố), người ta thường khởi tạo biến lưu trữ bằng `-1`. 
Số `-1` đóng vai trò là Cờ hiệu báo rằng "Tôi chưa tìm thấy gì cả".
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

## 5. CẤU TRÚC DỮ LIỆU NGĂN XẾP (Stack)

Ngăn xếp (Stack) hoạt động theo nguyên tắc **LIFO (Vào sau ra trước)** - Giống như xếp một chồng đĩa, cái đĩa nào đặt lên sau cùng sẽ bị lấy ra đầu tiên.
Kỹ thuật này chuyên trị các bài toán "Tìm cặp liền kề triệt tiêu nhau" hoặc "Kiểm tra ngoặc đóng mở".

Trong Python, mảng `List` sinh ra là để làm Stack hoàn hảo với chi phí O(1):
- `stack.append(x)`: Đặt `x` lên đỉnh.
- `stack.pop()`: Bốc phần tử trên đỉnh ra khỏi mảng và ném đi.
- `stack[-1]`: Nhìn trộm phần tử trên đỉnh (không vứt nó đi).

### Ví dụ: Xóa 2 số kề nhau có tổng chẵn (ICPC0101)
```python
stack = []
for x in a:
    # Nếu stack có đồ VÀ (x + đỉnh stack) chẵn -> Triệt tiêu!
    if stack and (x + stack[-1]) % 2 == 0:
        stack.pop()
    else:
        stack.append(x)
# Những gì còn sót lại trong stack chính là kết quả
print(len(stack))
```

---

## 6. TUYỆT KỸ BIẾN HÌNH CHUỖI (Replace & Split)

Khi bài toán yêu cầu "Trích xuất các đoạn SỐ được ngăn cách bởi các CHỮ CÁI" từ một chuỗi lộn xộn. 
Nếu dùng bạo lực (duyệt từng ký tự, gặp chữ thì gán `tmp = ""`...) sẽ cực kỳ dễ dính lỗi kẹt biến.

**Tư duy tối ưu:** "Hãy đấm mọi thứ không phải là số thành khoảng trắng!"

```python
s = "A129hG07bxjq3"

# Bước 1: Duyệt qua s, cái nào là số thì giữ, không thì biến thành " "
s_clean = "".join([c if c.isdigit() else " " for c in s])
# Kết quả s_clean: " 129  07    3"

# Bước 2: Dùng .split() tự động chẻ theo khoảng trắng, ép sang int (để tự mất số 0 ở đầu)
numbers = list(map(int, s_clean.split()))
# Kết quả: [129, 7, 3]
```
