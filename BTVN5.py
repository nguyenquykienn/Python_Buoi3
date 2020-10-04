print("-----ĐẾM CHỮ SỐ HOA VÀ CHỮ SỐ THƯỜNG-----")
def count_upper_lower(str):
    upper=lower=0
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print(f"Số chữ hoa: {upper}|Số chữ thường: {lower}")
str=input("Nhập chuỗi: ")
count_upper_lower(str)

