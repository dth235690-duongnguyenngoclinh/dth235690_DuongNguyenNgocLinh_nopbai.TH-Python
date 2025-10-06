print("Chương trình xác định quý trong năm")

thang = int(input("Nhập vào 1 tháng (1-12): "))

if thang in (1, 2, 3):
    print("Tháng", thang, "thuộc Quý 1")
elif thang in (4, 5, 6):
    print("Tháng", thang, "thuộc Quý 2")
elif thang in (7, 8, 9):
    print("Tháng", thang, "thuộc Quý 3")
elif thang in (10, 11, 12):
    print("Tháng", thang, "thuộc Quý 4")
else:
    print("Tháng không hợp lệ!")