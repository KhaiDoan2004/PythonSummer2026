scores = { 
    "An": [8, 7, 9], 
    "Bình": [6, 7, 5], 
    "Châu": [9, 8, 10] 
}

if __name__ == '__main__':
    for student, marks in scores.items():
        total = sum(marks)
        print(f"Tổng điểm của sinh viên {student} là: {total}")
