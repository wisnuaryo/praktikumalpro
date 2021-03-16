#71200663
#Wisnu Aryo Jatmiko

a= int(input("Masukan Jumlah Kolom: "))
b= ord("A")
for i in range(0,a):
    for j in range(0,i+1):
        c = chr(b)
        print(c, end=" ")
        b = b + 1
    print()