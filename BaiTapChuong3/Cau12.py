print("Bảng cửu chương từ 2 đến 9:")

for i in range(1, 11):          # i chạy từ 1 → 10 (hàng dọc)
    for j in range(2, 10):      # j chạy từ 2 → 9 (cột ngang)
        line = "{0}*{1:>2}={2:>2}".format(j, i, j*i)
        print(line, end="\t")   # in trên cùng 1 hàng, cách nhau bằng tab
    print()                     # xuống dòng sau khi in hết một hàng
