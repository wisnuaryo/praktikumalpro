#71200663
#Wisnu Aryo Jatmiko

def kubus(sisi):
    kubus = (sisi**3)
    print("Volume Kubus", kubus)

def balok(panjang,lebar,tinggi):
    balok = (panjang) * (lebar) * (tinggi)
    print("Volume Balok", balok)

def kerucut(jari,tinggi):
    kerucut = (1/3) * (3.14) * (jari**2) * (tinggi)
    print("Volume Kerucut", kerucut)

print("Selamat datang di kalkulator bangun ruang")
print("Silahkan Pilih menu: ")
print("1. Kubus")
print("2. Balok")
print("3. Kerucut")

x = input("Silahkan pilih menu(1/2/3): ")

if x == "1":
    a = float(input("Masukan sisi kubus: "))
    kubus(a)
elif x == "2":
    a = float(input("Masukan Panjang Balok: "))
    b = float(input("Masukan Lebar Balok: "))
    c = float(input("Masukan Tinggi Balok: "))
    balok(a,b,c)
elif x == "3":
    a = float(input("Masukan Jari - Jari Kerucut: "))
    b = a = float(input("Masukan Tinggi Kerucut: "))
    kerucut(a,b)
else:
    print("Maaf menu yang anda masukan tidak tersedia, mohon buat program sendiri")