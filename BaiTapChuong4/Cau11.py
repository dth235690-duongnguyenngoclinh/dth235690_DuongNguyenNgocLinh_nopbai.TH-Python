# cau11_sums_cases.py

def sum1(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += val
        val -= 1
    return s

def sum3():
    s = 0
    # lưu ý: vòng for dùng giá trị hiện tại của val, nhưng không thay đổi val
    for n in range(val, 0, -1):
        s += n
    return s

def run_case_1():
    global val
    print("=== Trường hợp 1 ===")
    val = 5
    print("val ban dau =", val)
    print("print(sum1(5)) ->", sum1(5))
    print("print(sum2())  ->", sum2())
    print("print(sum3())  ->", sum3())
    print("val sau cac goi =", val)
    print()

def run_case_2():
    global val
    print("=== Trường hợp 2 ===")
    val = 5
    print("val ban dau =", val)
    print("print(sum2())  ->", sum2())
    print("print(sum3())  ->", sum3())
    print("print(sum2())  ->", sum2())
    print("val sau cac goi =", val)
    print()

def run_case_3():
    global val
    print("=== Trường hợp 3 ===")
    val = 5
    print("val ban dau =", val)
    print("print(sum2())  ->", sum2())
    print("print(sum2())  ->", sum2())
    print("print(sum3())  ->", sum3())
    print("val sau cac goi =", val)
    print()

if __name__ == "__main__":
    run_case_1()
    run_case_2()
    run_case_3()
