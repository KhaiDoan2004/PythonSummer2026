# Đọc MONTHI.in
with open('MONTHI.in', 'r') as f:
    n_mon = int(f.readline().strip())
    subjects = {}
    for i in range(n_mon):
        ma = f.readline().strip()
        ten = f.readline().strip()
        hinh_thuc = f.readline().strip()
        subjects[ma] = ten

# Đọc CATHI.in
with open('CATHI.in', 'r') as f:
    n_ca = int(f.readline().strip())
    exams = {}
    for i in range(n_ca):
        date = f.readline().strip()
        t = f.readline().strip()
        room = f.readline().strip()
        
        d, m, y = map(int, date.split('/'))
        h, mi = map(int, t.split(':'))
        
        exam_id = f"C{i+1:03d}"
        date_out = f"{d:02d}/{m:02d}/{y:04d}"
        time_out = f"{h:02d}:{mi:02d}"
        
        exams[exam_id] = {
            'date': date_out,
            'time': time_out,
            'room': room,
            'key': (y, m, d, h, mi)
        }

# Đọc LICHTHI.in
with open('LICHTHI.in', 'r') as f:
    n_lich = int(f.readline().strip())
    schedule = []
    for i in range(n_lich):
        parts = f.readline().strip().split()
        ca_id = parts[0]
        mon_id = parts[1]
        nhom = parts[2]
        so_sv = parts[3]
        
        ca = exams[ca_id]
        ten_mon = subjects[mon_id]
        
        schedule.append((ca['key'], ca_id, ca['date'], ca['time'], ca['room'], ten_mon, nhom, so_sv))

schedule.sort()

for s in schedule:
    print(f"{s[2]} {s[3]} {s[4]} {s[5]} {s[6]} {s[7]}")
