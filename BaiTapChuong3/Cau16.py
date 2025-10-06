count = 0  # Biến đếm dấu *

for a in range(20, 100, 5):
    print('*', end='')
    count += 1

print()
print("Có", count, "dấu * được in ra trên màn hình")