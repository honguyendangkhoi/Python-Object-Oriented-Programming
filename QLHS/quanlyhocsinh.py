class hocsinh:
    def __init__(self, hovaten='', gioitinh='', lop='', stt=0):
        self.hovaten = hovaten
        self.gioitinh = gioitinh
        self.lop = lop
        self.stt = stt

    def nhapthongtin(self):
        try:
            self.hovaten = input("nhap ho va ten: ")
            self.gioitinh = input("nhap gioi tinh: ").lower()
            while self.gioitinh not in ['nam', 'nu']:
                self.gioitinh = input("nhap lai: ").lower()
            self.lop = int(input("nhap lop: "))
            self.stt = int(input("stt: "))
        except ValueError:
            print("vui long nhap dung dinh dang")
            self.nhapthongtin()


class diem(hocsinh):
    def diemtb(self):
        monhoc=["toan","van","anh","ly","hoa"]
        for sub in monhoc:
            while True:
                try:
                    score=float(input(f"nhap diem mon {sub}: "))
                    if 0<=score<=10:
                        setattr(self,sub,score)
                        break
                    else:
                        print("nhap lai")
                except ValueError:
                    print("nhap lai")
                    self.diemtb()

    def tinhdiem(self):
        return ((self.toan + self.van + self.anh + self.ly + self.hoa)/5)

    def xeploai(self):
        dtb = self.tinhdiem()
        if dtb >= 9:
            return "Xuat sac"
        elif dtb >= 8:
            return "Gioi"
        elif dtb >= 7:
            return "Kha"
        elif dtb >= 5:
            return "Trung binh"
        else:
            return "Yeu"


class PRINT(diem):
    def printinf(self):
        dtb = self.tinhdiem()
        print(f"Ho va Ten: {self.hovaten}, Lop: {self.lop},", 
            f"Gioi tinh:{self.gioitinh}, STT: {self.stt}",
            f"\nDiem toan: {self.toan} \nDiem van: {self.van}",
            f"\nDiem anh: {self.toan} \nDiem ly: {self.van}",
            f"\nDiem hoa: {self.toan}",
            f"\nDiem TB: {dtb:.2f}, Xep loai: {self.xeploai()}")

