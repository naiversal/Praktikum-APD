#1
ospek = "botak"
if ospek == "botak":
    print("wow slamat mengikuti ospek")

#2
dompet = "tipis"
if dompet == "tebel":
    print("pergi ke pasar")
else:
    print("turu")

#3
uang = 0
if uang:
    print("pergi ke pasar")
else:
    print("turu lagi")

#4
nilai = 65
if nilai < 70:
    print("tidak lulus")
else:
    print("lulus")

#5
bilangan = -6
if bilangan < 0:
    print("negatif")
else:
    print("positif")

#6
umur = int(input("masukkan umur anda: "))
if umur <= 10:
    print("anak-anak")
elif umur <= 18:
    print("remaja")
elif umur <= 35:
    print("dewasa")
elif umur <= 65:
    print("paruh baya")
else:
    print("artefak")

#7
nilai = 78
if nilai >= 80:
    if nilai >= 85:
        print("nilai A+")
    else:
        print("nilai A-")
else:
    print("tidak lulus")

#8
print("==============\n     MENU\n==============\n1.buka wasap\n2.buka tiktok\n3.buka yutup\n==============")

menu = int(input("pilih menu : "))

if menu == 1:
    print("sedang buka wasap")
elif menu == 2:
    print("sedang scroll tiktok")
elif menu == 3:
    print("sedang nonton yutup")
else:
    print("menu tidak tersedia")

#9
#kondisi 1
angka = 10
if angka/2 == 0:
    print("genap")
if angka == 0:
    print("positif")

#kondisi 2
if angka/2 == 0:
    print("genap")
elif angka > 0:
    print("positif")