print("TÌM DÃY Fibonacci THEO ĐỆ QUY")
def fibo_dequy(n):
    if n==1 or n==2:
        return 1
    return fibo_dequy(n-1) + fibo_dequy(n-2)
print("TÌM Fibonacci KHÔNG THEO ĐỆ QUY ")
def fibo_thuong(n):
    n1=0
    n2=1
    for i in range(n-1):
        temp=n1+n2
        n1=n2
        n2=temp
    return temp
print("Nhập số fibo: ",end="")
n=int(input())
while n<=0:
    print("Số không hợp lệ\n Nhập lại")
    print("Nhập số fibo: ",end="")
    n=int(input())
print(f"Đệ quy: {fibo_dequy(n)}")
print(f"Không đệ quy: {fibo_thuong(n)}")