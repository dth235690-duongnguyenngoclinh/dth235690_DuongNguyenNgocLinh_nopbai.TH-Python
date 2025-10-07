print(" Trình bày ý nghĩa toán tử /, //, %, **, and, or, is ?")

print("1. Toán tử số học")
print("-/: Chia thực (trả về kết quả kiểu float)")
#VD: 5 / 2   # Kết quả: 2.5

print("-//: Chia lấy phần nguyên (floor division)")
#VD  7 // 2   # Kết quả: 3

print("-%: Lấy phần dư (modulo)")
#VD 9 % 2   # Kết quả: 1

print("-**: Lũy thừa (power)")
#VD 3 ** 2   # Kết quả: 9 (3 mũ 2)

print("2. Toán tử logic")
print("-and: Trả về True nếu cả hai điều kiện đều đúng.")
#VD (10 > 2) and (0 < 4)  # True
#VD (8 > 2) and (1 > 4)  # False
 
print("-or: Trả về True nếu ít nhất một điều kiện đúng.")
#VD (5 > 2) or (0 > 7)   # True
#VD (1 > 4) or (9 > 4)   # False

print("3. Toán tử định danh")
print("-is: So sánh xem hai biến có cùng tham chiếu đến một đối tượng trong bộ nhớ hay không")
#VD a = [1, 2, 3]
#   b = [1, 2, 3]
#   c = a

#  (a == b)  # True  (giá trị giống nhau)
#  (a is b)  # False (không cùng đối tượng trong bộ nhớ)
#  (a is c)  # True  (cùng tham chiếu đến một đối tượng)