def daoNguocChuoi(chuoi):
    return chuoi[::-1]

inputStr = input("Moi nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc la: ", daoNguocChuoi(inputStr))