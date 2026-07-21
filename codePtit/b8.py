with open('CATHI.in', 'r') as f:
    n = int(f.readline().strip())
    exams = []
    for i in range(n):
        date = f.readline().strip()
        t = f.readline().strip()
        room = f.readline().strip()
        
        d, m, y = map(int, date.split('/'))
        h, mi = map(int, t.split(':'))
        
        date_out = f"{d:02d}/{m:02d}/{y:04d}"
        time_out = f"{h:02d}:{mi:02d}"
        exam_id = f"C{i+1:03d}"
        
        exams.append((y, m, d, h, mi, exam_id, date_out, time_out, room))

exams.sort()

for e in exams:
    print(f"{e[5]} {e[6]} {e[7]} {e[8]}")
