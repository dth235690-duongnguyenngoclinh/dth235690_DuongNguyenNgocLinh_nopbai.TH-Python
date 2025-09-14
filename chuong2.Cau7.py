print("Trình bày một số cách nhập dữ liệu từ bàn phím?")

print("1.Nhập dữ liệu kiểu chuỗi (string)") 
print("-input() luôn trả về chuỗi (str)")
#VD   nhon = input("Nhập tên của bạn: ")
#     print("Xin chào,", nhon)

print("2. Nhập số nguyên (int)")
print("-Dùng hàm int() để chuyển đổi chuỗi nhập vào thành số nguyên.")
#VD   age = int(input("Nhập tuổi của bạn: "))
#     print("Bạn", age, "tuổi")

print("3. Nhập số thực (float)")
print("-Dùng hàm float() để chuyển đổi chuỗi nhập vào thành số thực.")
#VD   score = float(input("Nhập điểm trung bình: "))
#     print("Điểm của bạn là:", score)

print("4. Nhập nhiều giá trị trên một dòng")
print("-Có thể dùng split() để tách chuỗi theo khoảng trắng.")
#VD   a, b = input("Nhập hai số cách nhau bởi dấu cách: ")
#     a = int(a)
#     b = int(b)
#     print("Tổng =", a + b)

print("5. Nhập nhiều số cùng lúc và chuyển kiểu dữ liệu")
print("-Kết hợp map() với split().")
#VD   numbers = list(map(int, input("Nhập các số nguyên: ").split()))
#     print("Danh sách vừa nhập:", numbers)

print("6. Nhập theo từng dòng (dùng vòng lặp)")
#VD   n = int(input("Nhập số phần tử: "))
#     arr = []
#     for i in range(n):
#        x = int(input(f"Nhập phần tử thứ {i+1}: "))
#        arr.append(x)
#     print("Danh sách:", arr)
