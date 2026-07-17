import math

# 1. Tính số n!
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 2. Kiểm tra xem n có phải là số nguyên tố không
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 4. Tính tổng các chữ số của 1 số
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# 3. Kiểm tra tổng các chữ số có phải là số nguyên tố hay không
def sum_of_digits_is_prime(n):
    total = sum_of_digits(n)
    return is_prime(total)

# 5. Kiểm tra xem n có phải là số palindrom không?
def is_palindrome(n):
    s = str(abs(n))
    return s == s[::-1]

if __name__ == '__main__':
    try:
        n = int(input("Nhập số nguyên dương n: "))
        print(f"1. {n}! = {factorial(n)}")
        print(f"2. {n} có phải là số nguyên tố không: {is_prime(n)}")
        print(f"3. Tổng các chữ số của {n} có phải số nguyên tố không: {sum_of_digits_is_prime(n)}")
        print(f"4. Tổng các chữ số của {n} = {sum_of_digits(n)}")
        print(f"5. {n} có phải là số palindrome không: {is_palindrome(n)}")
    except ValueError:
        print("Vui lòng nhập số nguyên.")
