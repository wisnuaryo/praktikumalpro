#71200663
#Wisnu Aryo Jatmiko

a = int(input("Masuka Bilangan Yang Akan Di-Check: "))
if a > 1:
    for i in range (2,a):
        if (a % i) == 0:
            print("Bilangan Tersebut Bukan Merupakan Bilangan Prima")
            break
    else:
        print("Bilangan Tersebut Merupakan Bilangan Prima")
else:
    print("Bilangan Tersebut Bukan Merupakan Bilangan Prima")