def tinhTongSoChan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

# Nhập danh sách từ người dùng và xử lí chuỗi
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))

# Sử dụng hàm và in kết quả
tongChan = tinhTongSoChan(numbers)
print("Tong cac so chan trong list la: ", tongChan)


