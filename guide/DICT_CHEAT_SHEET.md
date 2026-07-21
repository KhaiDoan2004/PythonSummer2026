# PYTHON DICTIONARY & TUPLE CHEATSHEET (BÍ KÍP TỪ ĐIỂN VÀ CẶP)

## 1. Bản chất của Từ Điển (Dictionary)
- Mảng (List) giống như một **Đoàn Tàu**: Các toa được đánh số thứ tự (Index) `0, 1, 2, 3...`.
- Từ điển (Dictionary) giống như **Tủ Đồ Siêu Thị**: KHÔNG CÓ THỨ TỰ. Nó chỉ gồm nhiều Ngăn tủ, mỗi ngăn có dán **Nhãn (Key)** và chứa **Đồ vật (Value)**.
- Cú pháp tạo: `dem = {'a': 1, 'b': 2}`

## 2. Bản chất của Tuple (Ngoặc Tròn) vs List (Ngoặc Vuông)
- **List (Mảng)**: Dùng ngoặc vuông `[1, 2, 3]`. Mềm dẻo, có thể tùy ý sửa đổi, thêm (`append`), xóa (`pop`).
- **Tuple (Bộ/Cặp)**: Dùng ngoặc tròn `(1, 2, 3)`. Bị "đổ bê tông", **bất tử và không thể thay đổi**. Chạy cực kỳ nhanh và thường được dùng để đóng gói dữ liệu trên đường vận chuyển (đảm bảo không rớt mất).

## 3. Ba phép thuật moi móc Từ điển
Với một từ điển `dem = {'a': 10, 'b': 5}`:
1. `dem.keys()`: Chỉ lột lấy bộ Nhãn dán $\rightarrow$ `['a', 'b']`
2. `dem.values()`: Chỉ moi lấy Đồ vật $\rightarrow$ `[10, 5]`
3. `dem.items()`: Bốc nguyên cả cụm (Nhãn, Đồ vật) bị gói chặt trong Tuple $\rightarrow$ `[('a', 10), ('b', 5)]`

## 4. Vòng lặp tối thượng cho Từ điển
Vì không có số thứ tự, tuyệt đối KHÔNG dùng `range()`. Ta phải dùng `.items()` để thò 2 tay ra đỡ lấy Nhãn và Đồ vật:
```python
dem = {'a': 10, 'b': 5}
for nhan_dan, do_vat in dem.items():
    print(f"Nhãn {nhan_dan} chứa {do_vat}")
```

## 5. Vũ Khí Hạng Nặng: COUNTER (Người đếm)
Thay vì dùng `a.count(x)` bên trong vòng `for` (Gây lỗi TLE vì tốn thời gian $O(N^2)$), hãy dùng `Counter`. Nó quét qua mảng đúng 1 lần ($O(N)$) và tự lập thành Từ điển.

```python
from collections import Counter

a = ['4', '4', '3', '2']
dem = Counter(a)  # Kết quả: {'4': 2, '3': 1, '2': 1}
```

### Cách tìm kẻ xuất hiện nhiều nhất (Value lớn nhất):

**Cách 1 (Dễ hiểu, Cốt lõi):**
```python
so_lan_max = 0
thang_nhieu_nhat = ""

for key, value in dem.items():
    if value > so_lan_max:
        so_lan_max = value
        thang_nhieu_nhat = key
```

**Cách 2 (Hacker Python - Dùng max với Key):**
Dùng hàm `max` ép nó so sánh dựa trên Value:
```python
thang_nhieu_nhat = max(dem, key=dem.get)
so_lan = dem[thang_nhieu_nhat]
```

**Cách 3 (Tuyệt kỹ Bóc Gói `most_common`):**
```python
# Lệnh most_common(1) trả về Mảng chứa 1 Tuple: [('4', 2)]
# Thêm [0] để bóc lớp Mảng (Ngoặc vuông) -> Lộ ra Tuple ('4', 2)
# Khai báo 2 biến để hứng 2 giá trị trong Tuple
thang_nhieu_nhat, so_lan = dem.most_common(1)[0]
```
