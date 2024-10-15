import os
data_pelanggan = [
    {
    "Nama" : "San",
    "Tanggal" : "1 Oktober 2024",
    "Paket" : "Foto wisuda",
    "Harga" : "Rp180000"
    },

    {
    "Nama" : "Wooyoung",
    "Tanggal" : "3 Oktober 2024",
    "Paket" : "Foto kelas",
    "Harga" : "Rp250000"    
    },

    {
    "Nama" : "Seonghwa",
    "Tanggal" : "6 Oktober 2024",
    "Paket" : "Foto keluarga",
    "Harga" : "Rp300000"
    },

    {
    "Nama" : "Hongjoong",
    "Tanggal" : "8 Oktober 2024",
    "Paket" : "Self photo",
    "Harga" : "Rp100000"
    },
]
os.system('cls || clear')

while True:
    print("""
=======================================
                 MENU
=======================================
1. Lihat data pelanggan
2. Buat data pelanggan baru
3. Perbarui data pelanggan
4. Hapus pelanggan yang sudah selesai
5. keluar dari program
=======================================""")
    menu = input("Pilih menu: ")
    os.system('cls || clear')

    match(menu):
        case "1":
            print("""
==============================
      LIHAT DATA PELANGGAN
==============================""")
            for index in range(len(data_pelanggan)):
                print(f"Data pelanggan ke-{index+1}")
                print(f"Nama pelanggan: {data_pelanggan[index]['Nama']}")
                print(f"Tanggal booking: {data_pelanggan[index]['Tanggal']}")
                print(f"Paket foto: {data_pelanggan[index]['Paket']}")
                print(f"Total bayar: Rp{data_pelanggan[index]['Harga']}")
                print("="*30)
            input("Tekan enter untuk memilih menu lagi...")
            os.system('cls || clear')
            
        case "2":
            print("""
==============================
   BUAT DATA PELANGGAN BARU    
==============================""")
            pelanggan_baru = input("Masukkan nama pelanggan baru: ")
            tanggal_baru = input("Masukkan tanggal booking: ")
            paket_foto = input("Masukkan paket foto: ")
            harga_bayar = int(input("Masukkan harga paket: Rp"))
            data_pelanggan.append({
                "Nama" : pelanggan_baru,
                "Tanggal" : tanggal_baru,
                "Paket" : paket_foto, 
                "Harga" : harga_bayar
            })
            print(f"Data pelanggan baru atas nama {pelanggan_baru} telah berhasil ditambahkan")
            input("Tekan enter untuk memilih menu lagi...")
            os.system('cls || clear')

        case "3":
            print("""
==============================
    PERBARUI DATA PELANGGAN   
==============================""")
            for index in range(len(data_pelanggan)):
                print(f"Data ke-{index+1}")
                print(f"Nama: {data_pelanggan[index]['Nama']}")
                print(f"Tanggal: {data_pelanggan[index]['Tanggal']}")
                print(f"Paket: {data_pelanggan[index]['Paket']}")
                print(f"Total Bayar: Rp{data_pelanggan[index]['Harga']}")
                print("="*30)
            index_edit = int(input("Masukkan nomor pelanggan yang ingin diubah: ")) - 1
            if 0 <= index_edit < len(data_pelanggan):
                nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
                tanggal_baru = input("Masukkan tanggal booking baru (kosongkan jika tidak ingin mengubah): ")
                paket_baru = input("Masukkan paket foto baru (kosongkan jika tidak ingin mengubah): ")
                harga_baru = input("Masukkan harga baru (kosongkan jika tidak ingin mengubah): ")

                if nama_baru:
                    data_pelanggan[index_edit]["Nama"] = nama_baru
                if tanggal_baru:
                    data_pelanggan[index_edit]["Tanggal"] = tanggal_baru
                if paket_baru:
                    data_pelanggan[index_edit]["Paket"] = paket_baru
                if harga_baru:
                    data_pelanggan[index_edit]["Harga"] = harga_baru

                print(f"Data pelanggan atas nama {nama_baru} berhasil diperbarui")
            else:
                print("Nomor pelanggan tidak valid.")
            input("Tekan enter untuk kembali ke menu...")
            os.system('cls || clear')

        case "4":
            print("""
==============================
    HAPUS DATA PELANGGAN   
==============================""")
            for index in range(len(data_pelanggan)):
                print(f"Data ke-{index+1}")
                print(f"Nama: {data_pelanggan[index]['Nama']}")
                print(f"Tanggal: {data_pelanggan[index]['Tanggal']}")
                print(f"Paket: {data_pelanggan[index]['Paket']}")
                print(f"Total Bayar: Rp{data_pelanggan[index]['Harga']}")
                print("="*30)
            index_hapus = int(input("Masukkan nomor pelanggan yang ingin dihapus: ")) - 1
            if 0 <= index_hapus < len(data_pelanggan):
                pelanggan_dihapus = data_pelanggan.pop(index_hapus)
                print(f"Pelanggan atas nama {pelanggan_dihapus['Nama']} berhasil dihapus.")
            else:
                print("Nomor pelanggan tidak valid.")

            input("Tekan enter untuk memilih menu lagi...")
            os.system('cls || clear')

        case "5":
            print("Keluar dari program")
            exit()

        case _:
            print(f"Menu {menu} tidak tersedia, silahkan pilih menu ulang")
            input("Tekan enter untuk memilih menu lagi...")
            os.system('cls || clear')
