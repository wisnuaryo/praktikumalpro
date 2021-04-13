#71200663
#Wisnu Aryo Jatmiko
from random import choice
char = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = int(input("Masukan Jumlah Character: "))
b = ''
file = open('pwandi.txt', 'w')
for i in range(a):
    b = choice(char)
    c = str(b)
    print(b, end='')
    file.write(c)

file.close()