import math
def S_of_n(n):
    #trả về s(n)=sqrt(2+sqrt(2+..)) với n dấu căn
    if n<= 0:
        raise ValueError("n phải là số nguyên dương (>=1).")
    s = 0.0
    for _ in range(n):
        s = math.sqrt(2+s)
    return s
def main():
    try:
        n = int(input("Nhập n(số dấu căn): ").strip())
    except ValueError:
        print("Vuilonfg nhập số nguyên dương.")
        return
    if n <= 0:
        print("n phải >=1.")
        return
    value = S_of_n(n)
    print(f"S({n})={value:.10f}")
if __name__ == "__main__":
    main()