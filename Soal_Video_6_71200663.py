#71200663
#Wisnu Aryo Jatmiko 
hp = 900
while hp > 0:
    if hp > 0:
        a = input("Masukan huruf yang akan di-identifikasi: ")
        b = ''
        for i in a:
            if i not in b:
                b = b + i
        print(b)
        hp = hp - 100
        print("Monster menerima 100 damage dari kamu, HP monster tersisa", hp)
        if hp == 0:
            print("Kamu telah berhasil mengalahkan monster tersebut")
            print("Selamat kamu telah menjadi pahlawan bagi penduduk desa")