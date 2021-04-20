#71200663
#Wisnu Aryo Jatmiko
a = []
b = []
k = int(input("Masukan Jumlah siswa laki - laki: "))
p = int(input("Masukan Jumlah siswa perempuan: "))

for i in range(k):
    c = int(input("Masukan berat badan siswa laki - laki: "))
    a.append(c)

for i in range(p):
    d = int(input("Masukan berat badan siswa perempuan: "))
    b.append(d)

e = a + b
e.sort()
Max = max(e)
Min = min(e)
jml = sum(e)
rata = jml / len(e)
print("List berat badan siswa laki-laki",a)
print("List berat badan siswa perempuan",b)
print("List berat badan semua siswa kelas A", e)
print("Berat badan terbesar siswa kelas A adalah", Max,"kilogram")
print("Berat badan terkecil siswa kelas A adalah", Min,"kilogram")
print("Rata - rata berat badan siswa kelas A adalah", rata, "kilogram")