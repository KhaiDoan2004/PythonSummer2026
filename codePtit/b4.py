from decimal import Decimal, ROUND_HALF_UP

class Student:
    def __init__(self, idx, name, scores):
        self.id = f"HS{idx:02d}"
        self.name = name
        total = scores[0]*2 + scores[1]*2 + sum(scores[2:])
        self.gpa = (total / Decimal('12')).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        
        if self.gpa >= Decimal('9.0'):
            self.rank = "XUAT SAC"
        elif self.gpa >= Decimal('8.0'):
            self.rank = "GIOI"
        elif self.gpa >= Decimal('7.0'):
            self.rank = "KHA"
        elif self.gpa >= Decimal('5.0'):
            self.rank = "TB"
        else:
            self.rank = "YEU"
            
    def __lt__(self, other):
        if self.gpa != other.gpa:
            return self.gpa > other.gpa
        return self.id < other.id

n = int(input())
students = []
for i in range(1, n + 1):
    name = input().strip()
    scores = [Decimal(x) for x in input().split()]
    students.append(Student(i, name, scores))

students.sort()

for s in students:
    print(f"{s.id} {s.name} {s.gpa} {s.rank}")
