import random
print("Những giá trị có thể xuất hiện khi chạy randrange(0, 100) là:")
values = [4.4, 34, -1, 100, 0, 99]
for i in values:
   if isinstance(i, int) and 0 <= i < 100:
    print(i) 
