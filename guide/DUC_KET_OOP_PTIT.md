# Đúc kết 10 bài OOP - Những bẫy chết người trên PTIT

## 1. Input từ FILE hay từ BÀN PHÍM?

> **Bài học xương máu nhất đêm nay!**

- Nếu đề bài ghi rõ tên file (vd: `MONTHI.in`, `CATHI.in`) → **Phải dùng `open()` để đọc file**.
- Nếu đề bài chỉ nói "Dòng đầu ghi...", "Nhập vào..." → Dùng `input()` bình thường.
- Dấu hiệu nhận biết: Nộp bằng `input()` mà bị **RTE liên tục** dù code chạy ngon trên máy → 99% là phải đọc file.

```python
# Đọc từ file
with open('CATHI.in', 'r') as f:
    n = int(f.readline().strip())
    for i in range(n):
        line = f.readline().strip()

# Đọc từ bàn phím
n = int(input())
```

---

## 2. Chuẩn hóa Ngày/Giờ (Bơm số 0)

PTIT **rất hay** kiểm tra định dạng ngày tháng. Nếu input là `9/5/2023`, output bắt buộc phải là `09/05/2023`.

```python
d, m, y = map(int, date.split('/'))
date_out = f"{d:02d}/{m:02d}/{y:04d}"

h, mi = map(int, time.split(':'))
time_out = f"{h:02d}:{mi:02d}"
```

**Ghi nhớ**: `:02d` = ép thành 2 chữ số, thiếu thì bơm số 0 vào đầu.

---

## 3. Sắp xếp đa tiêu chí bằng Tuple

Python so sánh Tuple **từ trái qua phải**. Đây là vũ khí tối thượng để sort nhiều điều kiện cùng lúc.

```python
# Sắp xếp: Ngày tăng dần → Tên tăng dần → Số tập GIẢM dần
data.append((date_key, name, -episodes, ...))
data.sort()
```

**Mẹo kinh điển**: Muốn **giảm dần** thì thêm dấu **trừ** (`-episodes`). Python sẽ tự hiểu "số âm lớn nhất = giá trị nhỏ nhất = đứng đầu".

---

## 4. OOP cơ bản (Class + `__lt__`)

Khuôn mẫu chung cho mọi bài OOP trên PTIT:

```python
class Student:
    def __init__(self, idx, name, score):
        self.id = f"HS{idx:02d}"
        self.name = name
        self.score = score
    
    # Hàm ma thuật: Dạy Python cách so sánh 2 đối tượng
    def __lt__(self, other):
        if self.score != other.score:
            return self.score > other.score  # Điểm cao đứng trước
        return self.id < other.id            # Bằng điểm thì ID nhỏ trước

students.sort()  # Python tự dùng __lt__ để sắp xếp
```

---

## 5. Làm tròn số (Decimal vs Float)

| Tình huống | Dùng gì |
|---|---|
| Chia 2 (kết quả đơn giản) | `float` + `:.2f` là đủ |
| Chia 12, chia 7... (số lẻ vô hạn) | **Bắt buộc** dùng `Decimal` + `ROUND_HALF_UP` |

```python
from decimal import Decimal, ROUND_HALF_UP

gpa = (total / Decimal('12')).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
```

**Lý do**: Python mặc định dùng Banker's Rounding (7.65 → 7.6). PTIT muốn Half-Up (7.65 → 7.7).

---

## 6. Tính thời gian (Quy hết ra phút)

Gặp bài tính giờ:phút → **Đổi tất cả ra phút**, tính xong rồi đổi ngược lại.

```python
# Đổi ra phút
total = h * 60 + m

# Đổi ngược lại
gio = total // 60
phut = total % 60
```

---

## 7. Parsing dòng có tên chứa dấu cách

Khi một dòng input chứa tên (có dấu cách) lẫn với các thông tin khác:

```python
parts = line.split()
# Token đầu = mã, Token thứ 2 = ngày, Token cuối = số
# Tất cả ở giữa = tên (có dấu cách)
ma = parts[0]
ngay = parts[1]
so = int(parts[-1])
ten = ' '.join(parts[2:-1])
```

---

## 8. Mã tự động tăng (ID formatting)

```python
f"HS{i:02d}"   # HS01, HS02, ..., HS99
f"C{i:03d}"    # C001, C002, ..., C999
f"P{i:03d}"    # P001, P002, ..., P999
f"TL{i:03d}"   # TL001, TL002, ...
```

---

## Bảng tổng kết chiến dịch

| Bài | Kết quả | Bẫy chính |
|-----|---------|-----------|
| b4 - Bảng điểm | ✅ AC | Decimal ROUND_HALF_UP, __lt__ |
| b5 - Tiền nước | ✅ AC | Giá bậc thang, round() |
| b6 - Tuyển NV | ❌ WA | Chưa rõ nguyên nhân (cần đề gốc) |
| b7 - Quán Game | ✅ AC | Quy ra phút, sys.stdin không cần |
| b8 - Ca thi | ❌ RTE→? | **Đọc từ file CATHI.in** |
| b9 - Lịch thi | ✅ AC | **Đọc từ 3 file .in** |
| b10 - Hệ thống phim | ✅ AC | Mỗi phim 4 dòng riêng, không phải 1 dòng |
