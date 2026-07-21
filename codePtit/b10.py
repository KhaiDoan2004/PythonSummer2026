n, m = map(int, input().split())

genres = {}
for i in range(1, n + 1):
    code = f"TL{i:03d}"
    genres[code] = input().strip()

movies = []
for j in range(m):
    genre_code = input().strip()
    date_str = input().strip()
    movie_name = input().strip()
    episodes = int(input().strip())
    
    movie_id = f"P{j+1:03d}"
    genre_name = genres[genre_code]
    
    d, mo, y = map(int, date_str.split('/'))
    date_key = (y, mo, d)
    date_out = f"{d:02d}/{mo:02d}/{y:04d}"
    
    movies.append((date_key, movie_name, -episodes, movie_id, genre_name, date_out, episodes))

movies.sort()

for mv in movies:
    date_key, name, neg_ep, mid, gname, date_out, episodes = mv
    print(f"{mid} {gname} {date_out} {name} {episodes}")
