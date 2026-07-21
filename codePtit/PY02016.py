from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    # Ta lấy luôn xâu dạng chữ, khỏi cần ép sang mảng số int cho đỡ tốn CPU
    a = input().split()
    
    # 1. Gọi vũ khí hạng nặng: Đếm toàn bộ mảng chỉ trong 1 nốt nhạc
    dem = Counter(a)
    
    # 2. most_common(1) sẽ trả về 1 cái mảng chứa phần tử xuất hiện nhiều nhất. 
    # Ví dụ: [('4', 5)] -> Nghĩa là số '4' xuất hiện 5 lần
    thang_nhieu_nhat, so_lan = dem.most_common(1)[0]
    
    # 3. Phán xét cuối cùng
    if so_lan > n // 2:
        print(thang_nhieu_nhat)
    else:
        print("NO")
