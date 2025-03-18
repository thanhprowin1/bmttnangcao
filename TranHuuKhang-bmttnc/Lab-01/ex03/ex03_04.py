def truyCapPhanTu(tuple_data):
    fisrt_element = tuple_data[0]
    last_element = tuple_data[-1]
    return fisrt_element, last_element

# Nhập danh sách từ người dùng
input_tuple = eval(input("Nhap tuple, vi du (1, 2, 3`): "))
first, last = truyCapPhanTu(input_tuple)

# In kết quả
print("Phan tu dau tien: ", first)
print("Phan tu cuoi cung: ", last)

