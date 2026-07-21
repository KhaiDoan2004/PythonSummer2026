import sys

class Gamer:
    def __init__(self, gamer_id, name, start, end):
        self.id = gamer_id
        self.name = name
        
        h1, m1 = map(int, start.split(':'))
        h2, m2 = map(int, end.split(':'))
        
        self.total_minutes = (h2 * 60 + m2) - (h1 * 60 + m1)
        
    def __lt__(self, other):
        if self.total_minutes != other.total_minutes:
            return self.total_minutes > other.total_minutes
        return self.id < other.id

raw = sys.stdin.read().splitlines()
lines = [l.strip() for l in raw if l.strip()]

n = int(lines[0])
gamers = []
idx = 1
for i in range(n):
    gamer_id = lines[idx]
    name = lines[idx + 1]
    start = lines[idx + 2]
    end = lines[idx + 3]
    gamers.append(Gamer(gamer_id, name, start, end))
    idx += 4

gamers.sort()

for g in gamers:
    h = g.total_minutes // 60
    m = g.total_minutes % 60
    print(f"{g.id} {g.name} {h} gio {m} phut")

