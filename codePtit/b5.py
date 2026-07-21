class Customer:
    def __init__(self, idx, name, old, new):
        self.id = f"KH{idx:02d}"
        self.name = name
        
        usage = new - old
        if usage <= 50:
            price = usage * 100
            self.total = round(price * 1.02)
        elif usage <= 100:
            price = 50 * 100 + (usage - 50) * 150
            self.total = round(price * 1.03)
        else:
            price = 50 * 100 + 50 * 150 + (usage - 100) * 200
            self.total = round(price * 1.05)
            
    def __lt__(self, other):
        if self.total != other.total:
            return self.total > other.total
        return self.id < other.id

n = int(input())
customers = []
for i in range(1, n + 1):
    name = input().strip()
    old = int(input())
    new = int(input())
    customers.append(Customer(i, name, old, new))

customers.sort()

for c in customers:
    print(f"{c.id} {c.name} {c.total}")
