import os

def clear_screen():
    os.system('cls || clear')

def tampilkan_pelanggan():
    for index in range(len(nama_pelanggan)):
        print(f"Data pelanggan ke-{index+1}")
        print(f"Nama pelanggan: {nama_pelanggan[index]}")
        print(f"Tanggal: {tanggal_booking[index]}")
        print(f"Paket: {paket_foto[index]}")
        print(f"Total bayar: Rp{harga_paket[index]}")
        print("="*30)

def tambah_pelanggan():
    pelanggan_baru = input("Masukkan nama pelanggan baru: ")
    tanggal_baru = input("Masukkan tanggal booking: ")
    paket_baru = input("Masukkan paket foto: ")
    harga_baru = input("Masukkan harga paket: Rp")
    nama_pelanggan.append(pelanggan_baru)
    tanggal_booking.append(tanggal_baru)
    paket_foto.append(paket_baru)
    harga_paket.append(harga_baru)
    print(f"Data pelanggan baru atas nama {pelanggan_baru} berhasil ditambahkan!")

def edit_pelanggan():
    if 0 <= index_edit < len(nama_pelanggan):
        print(f"Data pelanggan: {nama_pelanggan[index_edit]}")
        pelanggan_baru = input(f"Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
        tanggal_baru = input(f"Masukkan tanggal booking baru (kosongkan jika tidak ingin mengubah): ")
        paket_baru = input(f"Masukkan paket foto baru (kosongkan jika tidak ingin mengubah): ")
        harga_baru = input(f"Masukkan harga paket baru (kosongkan jika tidak ingin mengubah): ")
        
        if pelanggan_baru:
            nama_pelanggan[index_edit] = pelanggan_baru
        if tanggal_baru:
            tanggal_booking[index_edit] = tanggal_baru
        if paket_baru:
            paket_foto[index_edit] = paket_baru
        if harga_baru:
            harga_paket[index_edit] = harga_baru

            print(f"Data pelanggan ke-{index_edit+1} atas nama {nama_pelanggan[index_edit]} berhasil diperbarui!")
    else:
        print("Nomor pelanggan tidak valid.")

def hapus_pelanggan():
    index_user = int(input("masukkan nomor pelanggan yang ingin dihapus: "))
    del_user = nama_pelanggan.pop(index_user-1)
    return del_user

def menu():
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

nama_pelanggan = ["San", "Wooyoung", "Seonghwa", "Hongjoong"]
tanggal_booking = ["1 Oktober 2024", "3 Oktober 2024", "6 Oktober 2024", "8 Oktober 2024"]
paket_foto = ["Foto Wisuda", "Foto Kelas", "Foto Keluarga", "Self-Photo"]
harga_paket = ["Rp180000", "Rp250000", "Rp300000", "Rp100000"]
clear_screen()

while True:
    menu()
    menu = input("Pilih menu: ")
    clear_screen()

    match():
        case "1":
            print("""
==============================
    LIHAT DATA PELANGGAN
==============================""")
            tampilkan_pelanggan()
            input("Tekan enter untuk memilih menu lagi...")
            clear_screen()
            
        case "2":
            print("""
==============================
BUAT DATA PELANGGAN BARU    
==============================""")
            pelanggan_baru = tambah_pelanggan()
            input("Tekan enter untuk memilih menu lagi...")
            clear_screen()

        case "3":
            print("""
==============================
    PERBARUI DATA PELANGGAN   
==============================""")
            tampilkan_pelanggan()
            index_edit = int(input("Pilih nomor pelanggan yang ingin diubah: ")) - 1
            edit_pelanggan()
            input("Tekan enter untuk memilih menu lagi...")
            os.system('cls || clear')

        case "4":
            print("""
==============================
    HAPUS DATA PELANGGAN   
==============================""")
            tampilkan_pelanggan()
            hapus = hapus_pelanggan()
            print(f"Data pelanggan atas nama {hapus} telah berhasil dihapus")
            input("Tekan enter untuk memilih menu lagi...")
            clear_screen()

        case "5":
            print("Keluar dari program")
            exit()

        case _:
            print(f"Menu {menu} tidak tersedia, silahkan pilih menu ulang")
            input("Tekan enter untuk memilih menu lagi...")
            clear_screen()