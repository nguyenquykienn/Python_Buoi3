print("----TÍNH TOÁN CHỈ SỐ BMI-------")
def body_mass_index(m,h):
    BMI=m/math.pow(h,2)
    return BMI
def bmi_information(m,h):
    bmi=body_mass_index(m,h)
    if bmi > 30:
        print("Béo phì")
    elif bmi >=25:
        print("Thừa cân")
    elif bmi >=18.5:
        print("Bình thường")
    else:
        print("Gầy")
m=float(input("Nhập cân nặng: "))
h=float(input("Nhập chiều cao: "))
while m<0 or h<0:
    print("Dữ liệu không hợp lệ\n Nhập lại")
    print("Cân nặng là: ",end="")
    m=float(input())
    print("Chiều cao là: ",end="")
    h=float(input())
bmi_information(m,h)