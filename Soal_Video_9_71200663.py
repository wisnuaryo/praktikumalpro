#71200663
#Wisnu Aryo Jatmiko

a = {}
print("Fruit Basket")
print("--------------")
print("1. Tambah Buah")
print("2. Hapus Buah")
print("3. Tampilkan Buah Yang Terdata")
print("4. Exit")

b = int(input("Masukan menu yang akan dipilih: "))

while b != 4:
    if b == 1:
        buah = input("Masukan Jenis Buah: ")
        bnyk = int(input("Masukan jumlah buah: "))
        a[buah] = bnyk
    elif b == 2:
        buah = input("Masukan Buah yang akan dihapus: ")
        del(a[buah])
    elif b == 3:
        for buah in a:
            print(buah,":",a[buah])
    elif b != 4:
        print("Maaf tuan menu yang anda belum tersedia, silahkan update berikutnya ya")
    b = int(input("\nMasukan menu yang akan dipilih: "))
else:
    print("Fruit Basket was closed")
