#71200663
#Wisnu Aryo Jatmiko
import re
file = open("plat.txt","r")
for line in file:
    line = line.rstrip()
    if re.search(r'^[B]{1}\s{1}\d{1,4}\s{1}[A-Z]{1,3}', line):
        print(line,": Merupakan Plat Nomor Jakarta")
    else:
        print(line,": Bukan merupakan Plat Nomor Jakarta")
