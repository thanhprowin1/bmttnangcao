def xoaPhanTu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
# Sử dụng hàm và in kết quả
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keyToDelete = 'b'
result = xoaPhanTu(my_dict, keyToDelete)    
if result:
    print("Phan tu da duoc xoa tu Dictionary: ", my_dict)
else:
    print("Khong tim thay phan tu can xoa trong Dictionary.") 