# PYTHON STRING CHEATSHEET (BÍ KÍP XỬ LÝ XÂU)

## 1. Kiểm tra đặc tính của ký tự / xâu
- `s.isupper()`: Trả về True nếu TẤT CẢ chữ cái là in HOA.
- `s.islower()`: Trả về True nếu TẤT CẢ chữ cái là in thường.
- `s.isdigit()`: Trả về True nếu toàn bộ là CÁC CON SỐ.
- `s.isalpha()`: Trả về True nếu toàn bộ là CHỮ CÁI.
- `s.isalnum()`: Trả về True nếu toàn bộ là CHỮ CÁI hoặc SỐ (không có ký tự đặc biệt).

## 2. Biến hình xâu (Chuyển đổi Hoa/Thường)
- `s.upper()`: Biến tất cả thành IN HOA (VD: "hello" -> "HELLO").
- `s.lower()`: Biến tất cả thành in thường (VD: "HELLO" -> "hello").
- `s.title()`: Viết hoa chữ cái ĐẦU của MỖI TỪ (VD: "hello world" -> "Hello World").
- `s.capitalize()`: Chỉ viết hoa chữ cái ĐẦU TIÊN của CẢ XÂU (VD: "hello world" -> "Hello world").
- `s.swapcase()`: Hoa thành thường, thường thành Hoa (VD: "aBc" -> "AbC").

## 3. Cắt và Ghép xâu (Split & Join)
- `s.split()`: Cắt xâu thành một Mảng (List) các từ, mặc định cắt theo khoảng trắng.
  - VD: `"Le Trung Toan".split()` -> `['Le', 'Trung', 'Toan']`
- `s.split('/')`: Cắt xâu theo một ký tự cụ thể.
  - VD: `"25/11/2021".split('/')` -> `['25', '11', '2021']`
- `" ".join(mang)`: Ghép một mảng thành xâu, ở giữa là khoảng trắng (hoặc bất kỳ ký tự nào trong ngoặc kép).
  - VD: `" ".join(['Le', 'Trung', 'Toan'])` -> `"Le Trung Toan"`

## 4. Kỹ thuật Đếm cực nhanh
- Đếm chữ cái viết hoa trong xâu:
  `so_hoa = sum(1 for char in s if char.isupper())`
- Đếm chữ cái viết thường:
  `so_thuong = sum(1 for char in s if char.islower())`

## 5. Tuyệt kỹ Cắt và Chèn xâu (Slicing)
Xâu trong Python là **Bất biến (Giống hệt Tuple)**, tức là ngài cấm được dùng lệnh `insert()` để chèn trực tiếp.
Để chèn xâu `s2` vào xâu `s1` ở vị trí `p` (p tính từ 1), ta phải chặt `s1` làm đôi rồi nhét `s2` vào giữa:
- Cú pháp: `s_moi = s1[:p-1] + s2 + s1[p-1:]`
  - `s1[:p-1]`: Lấy nửa đầu của S1 (Từ đầu đến trước vị trí chèn)
  - `s2`: Xâu nhét vào giữa
  - `s1[p-1:]`: Lấy nửa sau của S1 (Từ vị trí chèn đến hết)
  `so_thuong = sum(1 for char in s if char.islower())`
- Đếm số lần xuất hiện của 1 từ/ký tự cụ thể:
  `s.count('a')` -> Đếm xem có bao nhiêu chữ 'a' trong xâu.

## 5. Cắt lát (Slicing) - Vũ khí tối thượng
Cú pháp: `s[start : stop : step]`
- Lật ngược xâu: `s[::-1]` (Rất hay dùng kiểm tra số thuận nghịch).
- Lấy 3 ký tự đầu: `s[:3]`.
- Lấy 3 ký tự cuối: `s[-3:]`.
- Xóa khoảng trắng 2 đầu: `s.strip()`.
