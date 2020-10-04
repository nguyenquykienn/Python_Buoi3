import math
n = int(input("Nhập bán kính : "))
def DienTichHinhTron(r):
    s=math.pi*r*r
    return s
print(f"Dien tich hinh trong co ban kinh {n}: {DienTichHinhTron(n)}")