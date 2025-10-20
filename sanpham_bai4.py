# sanpham_bai4.py

class SanPham:
    # Hàm khởi tạo có 3 tham số
    def __init__(self, ten_sp, gia, giam_gia):
        # Dùng private attribute
        self.__ten_sp = ten_sp
        self.__gia = float(gia)
        self.__giam_gia = float(giam_gia)

    # Getter & Setter (nếu cần dùng lại ở bài sau)
    def get_ten_sp(self):
        return self.__ten_sp

    def set_ten_sp(self, ten_sp):
        self.__ten_sp = ten_sp

    def get_gia(self):
        return self.__gia

    def set_gia(self, gia):
        self.__gia = float(gia)

    def get_giam_gia(self):
        return self.__giam_gia

    def set_giam_gia(self, giam_gia):
        self.__giam_gia = float(giam_gia)

    # Phương thức tính thuế
    def tinh_thue(self):
        return 0.1 * self.__gia

    # Phương thức xuất thông tin
    def xuat(self):
        print("Tên sản phẩm   :", self.__ten_sp)
        print("Đơn giá        : {:,.2f}".format(self.__gia))
        print("Giảm giá       : {:,.2f}".format(self.__giam_gia))
        print("Thuế nhập khẩu : {:,.2f}".format(self.tinh_thue()))
        print("-" * 30)
