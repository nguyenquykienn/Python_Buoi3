# --------------TỔNG CÁC SỐ LẺ-------------
def Tongle():
  n= int(input("Nhập số lẻ: "))
  x = 0
  while n % 2 ==0:
    n= int(input("Nhập lại: "))
  for i in range(n):
     i += 1
     if i % 2 != 0:
      x += i
  print(f"Kết quả là: {x}")
Tongle()