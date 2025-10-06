n, m = 0, 100
while n != m:
    n = int(input("Nhập n: "))
    if n < 0:
        break  # thoát vòng lặp khi n âm
print("n =", n)