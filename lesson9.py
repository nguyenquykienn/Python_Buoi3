print("----------Bảng cửu chương-----------")
def Bangcuuchuong(n):
    for i in range(1,11):
        print(f"{n}*{i}={i*n}")
print("Nhập n: ",end="")
n=int(input())
Bangcuuchuong(n)