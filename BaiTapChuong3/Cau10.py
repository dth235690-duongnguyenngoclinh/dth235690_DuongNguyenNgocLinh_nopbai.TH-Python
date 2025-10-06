print("Chương trình tính dãy số S(x,n) = x^1/1! + x^2/2! + ... + x^n/n!")

x = int(input("Nhập x: "))
n = int(input("Nhập n: "))

s = 0
for i in range(1, n + 1):
    tu = x ** i  # tử số
    mau = 1
    for j in range(1, i + 1):  # tính i!
        mau *= j
    s += tu / mau

print("S({0},{1}) = {2}".format(x, n, s))