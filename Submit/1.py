def count_elements(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts

if __name__ == '__main__':
    try:
        user_input = input("Nhập danh sách số nguyên cách nhau bởi dấu cách: ")
        lst = [int(x) for x in user_input.split()]
        result = count_elements(lst)
        print("Output:", result)
    except ValueError:
        print("Vui lòng nhập các số nguyên hợp lệ.")
