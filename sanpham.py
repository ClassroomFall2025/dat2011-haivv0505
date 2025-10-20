# sanpham.py

class SanPham:
    """
    Lớp SanPham có 3 thuộc tính: ten, gia, giam_gia
    Phương thức:
      - tinh_thue(): trả về thuế nhập khẩu = 10% * giá
      - xuat(): in thông tin sản phẩm (tên, đơn giá, giảm giá, thuế nhập khẩu)
      - nhap(): (tùy chọn) nhập từ bàn phím để dùng cho Bài 2
    """

    def __init__(self, ten_sp="", gia=0.0, giam_gia=0.0):
        self.ten_sp = ten_sp
        self.gia = float(gia)
        self.giam_gia = float(giam_gia)

    def tinh_thue(self):
        """Tính thuế nhập khẩu = 10% của giá (trước khi giảm giá)."""
        return 0.10 * self.gia

    def xuat(self):
        """Xuất thông tin sản phẩm ra màn hình."""
        thue = self.tinh_thue()
        print("Tên sản phẩm   :", self.ten_sp)
        print("Đơn giá        : {:,.2f}".format(self.gia))
        print("Giảm giá       : {:,.2f}".format(self.giam_gia))
        print("Thuế nhập khẩu : {:,.2f}".format(thue))
        print("-" * 30)

    def nhap(self):
        """Nhập thông tin sản phẩm từ bàn phím (dùng cho Bài 2)."""
        self.ten_sp = input("Nhập tên sản phẩm: ").strip()
        # đảm bảo nhập số hợp lệ
        while True:
            try:
                self.gia = float(input("Nhập đơn giá: ").strip())
                break
            except ValueError:
                print("Giá phải là số. Thử lại.")
        while True:
            try:
                self.giam_gia = float(input("Nhập giảm giá: ").strip())
                break
            except ValueError:
                print("Giảm giá phải là số. Thử lại.")
