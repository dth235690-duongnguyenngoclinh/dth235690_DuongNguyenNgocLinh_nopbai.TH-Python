def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def so_ngay_trong_thang(thang, nam):
    if thang in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif thang in (4, 6, 9, 11):
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return 0  # tháng không hợp lệ

def ngay_ke_tiep(ngay, thang, nam):
    max_day = so_ngay_trong_thang(thang, nam)

    if max_day == 0 or ngay < 1 or ngay > max_day:
        return "Ngày không hợp lệ"

    if ngay < max_day:
        return f"{ngay+1}/{thang}/{nam}"
    else:
        if thang == 12:  # hết năm
            return f"1/1/{nam+1}"
        else:  # sang tháng mới
            return f"1/{thang+1}/{nam}"

# Ví dụ chạy thử
print(ngay_ke_tiep(28, 2, 2023))  # không nhuận
print(ngay_ke_tiep(28, 2, 2024))  # năm nhuận
print(ngay_ke_tiep(31, 12, 2023))
print(ngay_ke_tiep(30, 4, 2023))
print(ngay_ke_tiep(15, 8, 2023))