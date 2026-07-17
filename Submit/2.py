dictionary = {
    "hello": "xin chào",
    "world": "thế giới",
    "computer": "máy tính",
    "programming": "lập trình",
    "python": "ngôn ngữ lập trình python"
}

if __name__ == '__main__':
    word = input("Nhập từ tiếng Anh cần tra cứu: ").strip().lower()
    if word in dictionary:
        print(f"Nghĩa tiếng Việt: {dictionary[word]}")
    else:
        print("không tìm thấy")
