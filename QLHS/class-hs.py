from quanlyhocsinh import PRINT
ds=[]
while True:
    try:
        n = int(input("hay nhap so luong hoc sinh: "))
        if n > 0:
            break
        else:
            print("nhap lai: ")
    except:
        print("vui long nhap so nguyen")

for i in range(n):
    print(f"\n----Hoc sinh thu {i+1}----")
    hs=PRINT()
    hs.nhapthongtin()
    hs.diemtb()
    ds.append(hs)

print("\n====THONG TIN HOC SINH====")
for hs in ds:
    hs.printinf()
    print("/-----------------------------------------/")
