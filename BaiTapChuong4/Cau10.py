# cau10_sleep_shapes_fixed.py
import time, os, platform

def clear_screen():
    if platform.system().lower().startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

# 4 hình được mô tả bằng list các dòng (dùng '.' để tương ứng với chấm trong ảnh)
shape1 = [
"      .        ",
"      . .       ",
"      . . .      ",
". . . . . . .     ",
". . .      ",
". .       ",
".        "
]

shape2 = [
"      .        ",
"      . .       ",
"      .   .      ",
". . . . . . .     ",
".   .      ",
". .       ",
".        "
]

shape3 = [
"       . . . .    ",
"       . . .     ",
"       . .      ",
"       .       ",
"     . .      ",
"   . . .     ",
" . . . .    ",
]

shape4 = [
"       . . . .    ",
"       .   .     ",
"       . .      ",
"       .       ",
"     . .      ",
"   .   .     ",
" . . . .    ",
]

shapes = [shape1, shape2, shape3, shape4]

def print_shape(shape):
    for line in shape:
        print(line)

def main(delay=5):
    for i, shape in enumerate(shapes, start=1):
        clear_screen()
        print(f"Hình {i}:\n")
        print_shape(shape)
        time.sleep(delay)
    clear_screen()
    print("Hoàn thành - đã hiển thị 4 hình.")

if __name__ == "__main__":
    main()
