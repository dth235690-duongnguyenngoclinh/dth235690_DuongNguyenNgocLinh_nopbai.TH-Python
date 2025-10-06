a = 0
count = 0  # Đếm tổng số dấu *

while a < 100:
    b = 0
    while b < 40:
        if b % 20 == 2 or b % 20 == 0:
            print('*', end='')
            count += 1
        b = b + 1
    print()
    a = a + 1

print("Chương trình in ra", count, "dấu * (4 dấu mỗi dòng, 100 dòng)")
