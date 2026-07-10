# Bài 2: Tra cứu từ điển Anh–Việt

tu_dien = {
    "hello": "xin chào",
    "apple": "quả táo",
    "cat": "con mèo",
    "dog": "con chó",
    "book": "quyển sách"
}

tu_khoa = input("Nhập từ tiếng Anh cần tra: ").strip().lower()

if tu_khoa in tu_dien:
    print(f"Nghĩa của từ '{tu_khoa}' là: {tu_dien[tu_khoa]}")
else:
    print("không tìm thấy")
