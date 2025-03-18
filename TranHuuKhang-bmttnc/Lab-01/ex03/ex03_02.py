def daoNguocList(lst):
    return lst[::-1]

# Nhập danh sách từ người dùng và xử lí chuỗi
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))

# Sử dụng hàm và in kết quả
listDaoNguoc = daoNguocList(numbers)
print("Danh sach sau khi dao nguoc la: ", listDaoNguoc)