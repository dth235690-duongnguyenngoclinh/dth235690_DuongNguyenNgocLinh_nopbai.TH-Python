# Hình 1
n = int(input("Nhập n: "))
for i in range(n):
    print(' ' * i + '* ' * (n - i))

# Hình 2
print()
n = int(input("Nhập n: "))
for i in range(n):
    print(' ' * i + '*' + ' ' * (2 * (n - i - 1) - 1) + ('*' if i < n - 1 else ''))

# Hình 3
print()
n = int(input("Nhập n: "))
for i in range(n):
    print(' ' * i + '*' + (' ' * (2 * (n - i - 1) - 1) + '*' if i < n - 1 else ''))
