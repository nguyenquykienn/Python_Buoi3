print("---MA TRẬN---")
def create_matrix(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i*j,end="\t")
        print()
n=int(input("Số hàng là: "))
m=int(input("Số cột là: "))
create_matrix(n,m)
