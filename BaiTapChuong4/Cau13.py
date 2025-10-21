#(Số hoàn thiện là số có tổng các ước số của nó không kể chính nó bằng chính nó).
#(Số thịnh vượng là số có tổng các ước số của nó không kể chính nó lớn hơn chính nó).

#Hàm chính 
def sum_proper_divisors(n: int) -> int:
    #tính tổng các ước dướng của n nhưng không tính chính n.
    if n<= 1:
        return 0
    s = 1
    import math
    root = int (math.isqrt(n))
    for d in range(2,root+1):
        if n%d == 0:
            s += d
            other = n//d
            if other !=d:
                s +=other
    return s
#Hàm kiểm tra
#kiểm tra số hoàn thiện
def is_perfect(n: int) -> bool:
    return n>0 and sum_proper_divisors(n) == n
#kiểm tra số thịnh vượng
def is_abundant(n: int)->bool:
    return n>0 and sum_proper_divisors(n)>n
#hàm chạy thử
n = int(input("Nhập số nguyên dương n:"))
tong_uoc = sum_proper_divisors(n)
print(f"Tổng các ước (không kể {n})là: ", tong_uoc)

if is_perfect(n):
    print(f"-> {n} Là số hoàn thiện (Pểfect number).")
elif is_abundant(n):
    print(f"-> {n} Là số thịnh vượng (Abundant number).")
else:
    print(f"-> {n} Không phải hai loại trên")