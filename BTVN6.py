print("Chuỗi pangram")
def is_pangram(str, alphabet):
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
str=input("Nhập chuỗi kiểm tra: ")
alphabet="ABCDEFGHIKLMNOPQRSTUWXYZ"
if is_pangram(str,alphabet):
    print(f" \"{str}\" True")
else:
    print(f" \"{str}\" False")