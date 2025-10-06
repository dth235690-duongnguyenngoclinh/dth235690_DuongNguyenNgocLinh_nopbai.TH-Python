n = int(input("Nhập n: "))


print("Hình 1")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print()  # Dòng trống giữa hai hình


print("Hình 2:")
for i in range(n):
    # In khoảng trắng để đẩy tam giác sang phải
    for k in range(n - i - 1):
        print(' ', end=' ')
    # In phần tam giác
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()