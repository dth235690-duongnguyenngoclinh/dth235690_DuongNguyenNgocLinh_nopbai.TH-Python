import math

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for i in range(0, n + 1):
    tu = x ** (2 * i + 1)
    mau = math.factorial(2 * i + 1)
    S += tu / mau

print("Giá trị S =", S)