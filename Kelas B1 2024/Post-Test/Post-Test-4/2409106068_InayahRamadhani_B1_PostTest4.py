import os
os.system('cls')

print("Silahkan login terlebih dahulu.")

kesempatan = 3
while kesempatan > 0:
    username = input("masukkan username: ")
    password = input("masukkan password: ")

    if username == "inayah" and password == "068":
        print("berhasil login")
        break
    else:
        print("Username atau password salah, silahkan coba lagi")
        kesempatan -= 1
        print(f"Kesempatan tersisa {kesempatan} kali\n")
    if kesempatan == 0:
        print("Kesempatan habis. Program telah berhenti")
        break

if kesempatan > 0:
    while True:
        print("""
        ===============================================
            Menu Program Menghitung Luas Permukaan,
        Keliling dan Volume Berbagai Bangun Ruang
        ===============================================
            1. Luas permukaan kubus
            2. Keliling balok
            3. Luas permukaan tabung
            4. Volume limas segi empat
            5. Keluar dari menu
        ===============================================
        """)
        menu = (input("Pilih menu yang anda inginkan : "))

        os.system('cls')
        if menu == "1":
            print("Anda memilih menu : 1. Luas permukaan kubus")
            sisi = float(input("Masukkan panjang sisi kubus (dalam cm): "))
            LpKubus = 6*sisi**2
            print("Luas permukaan kubus : ", LpKubus, "cm^2")
        elif menu == "2":
            print("Anda memilih menu : 2. Keliling balok")
            panjang = float(input("Masukkan panjang balok (dalam cm): "))
            lebar = float(input("Masukkan lebar balok (dalam cm): "))
            tinggi = float(input("Masukkan tinggi balok (dalam cm): "))
            KBalok = 4*(panjang+lebar+tinggi)
            print("keliling balok : ", KBalok, "cm")
        elif menu == "3":
            print("Anda memilih menu: 3. Luas permukaan tabung")
            pi = 3.14
            tinggi = float(input("Masukkan tinggi (dalam cm): "))
            jarijari = float(input("Masukkan panjang jari-jari (dalam cm): "))
            LpTabung = 2*pi*jarijari*(jarijari+tinggi)
            print("luas permukaan tabung : ", LpTabung, "cm")
        elif menu == "4":
            print("Anda memilih menu: 4. Volume limas segi empat")
            sisi = float(input("Masukkan panjang sisi alas (dalam cm): "))
            tinggi = float(input("Masukkan tinggi (dalam cm): "))
            VLimas = (1/3)*(sisi**2)*tinggi
            print("Volume limas segi empat: ", VLimas, "cm^3")
        elif menu == "5":
            print("Anda memilih menu: 5. Keluar dari program")
            break
        else:
            print("Menu yang anda pilih: ", menu, "\nInput tidak valid. Silahkan masukkan menu kembali: ")
            continue

        pilih_lagi = input("\nApakah Anda ingin memilih menu lagi? (ya/tidak): ")
        if pilih_lagi == "ya":
            continue
        else:
            break

    print("Program telah berakhir. Terima kasih")