print("Đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước")
i=0
def count_odd(n,i):
    if i==len(n) or n[i].isnumeric==False:
        return 0
    if int(n[i])%2!=0:
        return 1+count_odd(n,i+1)
    else:
        return 0+count_odd(n,i+1)

n=input("Nhập số kiểm tra: ")
print(count_odd(n,i))
