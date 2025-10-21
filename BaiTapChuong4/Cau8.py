import math
def log_base(a, x):
    #assume a>0, a!=1, x>0
    return math.log(x) / math.log(a)
def main():
    try:
        x = float(input("Nhập x (x>0): ").strip())
        a = float(input("Nhập cơ số a (a>0 và a!=1): ").strip())
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
        return
    if x<=0:
        print("Lỗi: x phải > 0.")
        return
    if a<=0 or a==1:
        print("Lỗi: a phải > 0 và khác 1.")
        return
    result = log_base(a, x)
    print(f"log_{a}({x}) = {result:.6f}")
if __name__ == "__main__":
    main()