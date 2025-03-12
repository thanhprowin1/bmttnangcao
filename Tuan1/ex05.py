so_gio_lam= float(input("Nhập số giờ làm: "))
luong_gio = float(input("Nhập lương mỗi giờ: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0,so_gio_lam - gio_tieu_chuan)
thuc_linh = so_gio_lam * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"Thực lĩnh của bạn là:  {thuc_linh}")