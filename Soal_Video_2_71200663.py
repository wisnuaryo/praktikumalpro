#71200663
#Wisnu Aryo Jatmiko

print("Selamat Datang Pada Progam Kalkulator Sederhana")
print("Silahkan Pilih Menu Dibawah Ini: ")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

x = int(input("Silahkan pilih menu(1/2/3/4): "))
a = float(input("Masukan Angka: "))
b = float(input("Masukan Angka: "))

if x == 1:
    c = a + b
    print("Jadi, Hasil Penambahanya Adalah =", c)
elif x == 2:
    c = a - b
    print("Jadi, Hasil Penguranganya Adalah =", c)
elif x == 3:
    c = a * b
    print("Jadi, Hasil Perkalianya Adalah =", c)
elif x == 4:
    c = a / b
    print("Jadi, Hasil Pembagianya Adalah =", c)

