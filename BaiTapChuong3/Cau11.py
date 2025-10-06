print("Chương trình kiểm tra số nguyên tố")

while True:
    n = int(input("Nhập 1 số nguyên dương: "))

    if n < 2:
        print(n, "không phải là số nguyên tố")
    else:
        dem = 0
        for i in range(1, n + 1):
            if n % i == 0:
                dem += 1
        if dem == 2:
            print(n, "là số nguyên tố")
        else:
            print(n, "không phải là số nguyên tố")

    hoi = input("Tiếp tục không (c/k): ")
    if hoi.lower() == "k":   # dùng .lower() để nhận cả 'K' hoặc 'k'
        break

print("BYE!")
