def demSoLanXH(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Nhập danh sách từ người dùng
input_str = input("Nhap danh sach cac tu, cach nhau bang dau cach: ")
word_lst = input_str.split()

# Sử dụng hàm và in kết quả
soLanXH = demSoLanXH(word_lst)
print("So lan xuat hien cua cac phan tu: ",soLanXH)
