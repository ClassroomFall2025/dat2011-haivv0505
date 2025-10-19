class sinhvien:
    def __init__(self, ten_sinh_vien="", nam_sinh="", truong=""):
        self.ten_sinh_vien = ten_sinh_vien
        self.nam_sinh = nam_sinh
        self.truong = truong

    def them_sinhvien(self, ten, namsinh, truong):
        self.ten_sinh_vien = ten
        self.nam_sinh = namsinh
        self.truong = truong

    def xoa(self):
        # simple reset of attributes
        self.ten_sinh_vien = ""
        self.nam_sinh = ""
        self.truong = ""

    def sua(self, ten=None, namsinh=None, truong=None):
        if ten is not None:
            self.ten_sinh_vien = ten
        if namsinh is not None:
            self.nam_sinh = namsinh
        if truong is not None:
            self.truong = truong

    def xuat_thong_tin(self):
        print(f"Tên sinh viên: {self.ten_sinh_vien}, Năm sinh: {self.nam_sinh}, Trường: {self.truong}")


if __name__ == "__main__":
    sv1 = sinhvien()
    sv1.them_sinhvien("hoang", 2020, "FPT")
    print(sv1.ten_sinh_vien)
    sv1.xuat_thong_tin()
        

    
    