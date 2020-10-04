#-------------------KIEM TRA SO NGUYEN TO HAY KHONG-------------
n = int(input("Nhập vào số nguyên n:"))
if n <2:
    print("Nhập số lớn hơn hoặc bằng 2")
    exit()
Songuyento = True
for i in range(2, int(n/2) +1):
    if n % i ==0:
        Songuyento = False
        break
if Songuyento:
    print("Số %d là số nguyên tố" % n)
else:
    print("Số %d không phải là số nguyên tố" % n)