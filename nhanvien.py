class NhanVien:
    def __init__(self,maNV,ten,tuoi,diachi,luong,giolam):
        self.maNV = maNV
        self.ten=ten
        self.tuoi=tuoi
        self.diachi=diachi
        self.luong=luong
        self.giolam=giolam
    
    def inputInfo(self):
        try:
            self.maNV = int(input("Nhap ma NV: "))
            self.ten = input("Nhap ten: ")
            self.tuoi = int(input("Nhap tuoi: "))
            self.diachi = input("Nhap dia chi: ")
            self.luong = float(input("Nhap luong: "))
            self.giolam = float(input("Nhap gio lam: "))
        except ValueError:
            print("Nhap du lieu sai dinh dang!")
            self.inputInfo()


    def printInfo(self):
        print(f"ma nhan vien: {self.maNV}, ten: {self.ten}, tuoi: {self.tuoi}, "
              f"dia chi: {self.diachi}, luong: {self.luong}, gio lam: {self.giolam}")
    
    def tinhThuong(self):
        thuong=0
        if self.giolam>=200:
            thuong=self.luong*(self.luong*0.2)
        elif self.giolam<200 and self.giolam>=100:
            thuong=self.luong*(self.luong*0.1)
        else:
            thuong=0
        return thuong