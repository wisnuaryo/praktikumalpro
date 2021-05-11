#71200663
#Wisnu Aryo Jatmiko
def f(lst):
    listtostr = ' '.join([str(ele) for ele in lst])
    kset = set()
    for k in listtostr:
        if k in kset:
            pass
        else:
            kset.add(k)
    klist = list(kset)
    klist.sort()
    kstr = ' '.join(klist)
    for i in kstr:
        print(i+',',end='')

a = int(input("Panjang list: "))
b = []
for i in range(a):
    c = input("Masukan kata: ")
    b.append(c)
f(b)
