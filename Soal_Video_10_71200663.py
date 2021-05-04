#71200663
#Wisnu Aryo Jatmiko

print("Progam Tuple")
print('---------------')
print("1. Tambah Tuple")
print("2. Hapus Tuple")
print("3. Tampilkan Tuple")
print("4. Exit")

menu = int(input("Masukan menu yang dipilih: "))
tpl = ()

while menu != 4:
    if menu == 1:
        l = list(tpl)
        isi = input("Masukan tuple: ")
        l.append(isi)
        tpl = tuple(l)
    elif menu == 2:
        hps = input("Masukan tuple yang akan dihapus: ")
        l = list(tpl)
        l.remove(hps)
        tpl = tuple(l)
    elif menu == 3:
        print(tpl)
        print(type(tpl))
    elif menu != 4:
        print("Maaf tuanku menunya belum ada")
    menu = int(input("\nMasukan menu yang dipilih: "))
else:
    print("Progam tuple telah ditutup")