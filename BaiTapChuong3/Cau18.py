n = int(input("Nhập n: "))

# ---- Hình 1: hình vuông viền ----
print("Hình 1:")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()  # dòng trống giữa các hình

# ---- Hình 2: tam giác rỗng đẩy sang phải ----
print("Hình 2:")
for i in range(n):
    # in khoảng trắng để đẩy sang phải
    print(' ' * (n - i - 1), end='')
    # in tam giác rỗng (đầu, cạnh phải, hoặc hàng đáy đầy sao)
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

# ---- Hình 3: hai tam giác rỗng đối xứng qua trục ngang ----
print("Hình 3:")
width = 2 * n - 1
upper = []

# phần trên (n-1 dòng)
for i in range(1, n):
    line = [' '] * width
    line[0] = '*'                 # cạnh trái
    if i > 1:
        line[2 * (i - 1)] = '*'   # cạnh xiên phải (cách đều bằng 1 ô)
    upper.append(''.join(line))

# in phần trên
for ln in upper:
    print(ln)

# dòng giữa đầy sao
print('*' * width)

# phần dưới: phản chiếu ngang phần trên
for ln in reversed(upper):
    print(ln[::-1])
