import math 
def distance(xa, ya, xb, yb):
    return math.sqrt((xb - xa)**2 + (yb - ya)**2)
def main():
    try:
        xa = float(input("Nhập x_A: ").strip())
        ya = float(input("Nhập y_A: ").strip())
        xb = float(input("Nhập x_B: ").strip())
        yb = float(input("Nhập y_B: ").strip())
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
        return
    d = distance(xa, ya, xb, yb)
    print(f"Dộ dài doạn AB = {d:.4f}")
if __name__ == "__main__":
    main()