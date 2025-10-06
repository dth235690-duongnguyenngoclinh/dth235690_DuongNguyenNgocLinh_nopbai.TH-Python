# range(5): tạo dãy từ 0 → 4 (mặc định bắt đầu từ 0)
print("a:", list(range(5)))  # [0, 1, 2, 3, 4]

# range(5, 10): tạo dãy từ 5 → 9 (tăng 1 mỗi lần)
print("b:", list(range(5, 10)))  # [5, 6, 7, 8, 9]

# range(5, 20, 3): tạo dãy từ 5 → nhỏ hơn 20, bước nhảy +3
print("c:", list(range(5, 20, 3)))  # [5, 8, 11, 14, 17]

# range(20, 5, -1): tạo dãy giảm từ 20 → lớn hơn 5, bước nhảy -1
print("d:", list(range(20, 5, -1)))  # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

# range(20, 5, -3): tạo dãy giảm từ 20 → lớn hơn 5, bước nhảy -3
print("e:", list(range(20, 5, -3)))  # [20, 17, 14, 11, 8]

# range(10, 5): không có phần tử nào vì mặc định bước là +1 mà 10 > 5
print("f:", list(range(10, 5)))  # []

# range(0): không có phần tử vì kết thúc ngay tại 0
print("g:", list(range(0)))  # []

# range(10, 101, 10): tạo dãy từ 10 → 100, bước nhảy +10
print("h:", list(range(10, 101, 10)))  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# range(10, -1, -1): tạo dãy giảm từ 10 → 0
print("i:", list(range(10, -1, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# range(-3, 4): tạo dãy từ -3 → 3
print("j:", list(range(-3, 4)))  # [-3, -2, -1, 0, 1, 2, 3]

# range(0, 10, 1): từ 0 → 9, bước nhảy 1
print("k:", list(range(0, 10, 1)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]