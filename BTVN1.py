print("max min")
def max_min(*numbers):
    print(f"Day so duoc truyen vao: {numbers}")
    return max(numbers),min(numbers)
max,min=max_min(1,3,6,10,20,25,150)
print(f"max: {max}, min: {min}")