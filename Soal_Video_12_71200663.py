#71200663
#Wisnu Aryo Jatmiko
def comb(a):
    if a==0:
        return 1
    else:
        return a*comb(a-1)

a1 = int(input("Masukan jumlah kelereng: "))
a2 = int(input("Masukan jumlah pengambilan: "))
a3 = a1 - a2

b1 = comb(a1)
b2 = comb(a2)
b3 = comb(a3)

c = b1 // (b2*b3)

print("Banyak cara pengambilan kelereng adalah", c)