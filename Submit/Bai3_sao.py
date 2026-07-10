# Bài 3: Tổng điểm sinh viên

scores = { 
    "An": [8, 7, 9], 
    "Bình": [6, 7, 5], 
    "Châu": [9, 8, 10] 
}

for ten, danh_sach_diem in scores.items():
    tong = sum(danh_sach_diem)
    print(f"Tổng điểm của {ten} là: {tong}")
