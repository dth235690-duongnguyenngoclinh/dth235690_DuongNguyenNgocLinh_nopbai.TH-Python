def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    if n < 10:  # số có 1 chữ số
        return don_vi[n]

    elif n < 20:  # từ 10 đến 19
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        else:
            return "mười " + don_vi[n % 10]

    else:  # từ 20 đến 99
        chuc = n // 10
        dv = n % 10
        ket_qua = don_vi[chuc] + " mươi"

        if dv == 0:
            return ket_qua
        elif dv == 1:
            return ket_qua + " mốt"
        elif dv == 5:
            return ket_qua + " lăm"
        else:
            return ket_qua + " " + don_vi[dv]


# Thử chạy
for so in [5, 10, 15, 21, 35, 40, 99]:
    print(so, "→", doc_so(so))