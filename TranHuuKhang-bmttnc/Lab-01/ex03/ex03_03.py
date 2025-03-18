def taoTupleTuList(lst):
    return tuple(lst)

# Nhập danh sách từ người dùng và xử lí chuỗi
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = taoTupleTuList(numbers)
print("List: ", numbers)
print("Tuple tu list: ", my_tuple)