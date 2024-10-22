import os

data_login = {
    "admin" : {
        "username" : "admin",
        "password" : "admin123"
    },
    "user" : {
        "username" : "user",
        "password" : "user123"
    }
}

data_pelanggan = [
    {
        "Nama": "San",
        "Tanggal": "1 Oktober 2024",
        "Paket": "Foto wisuda",
        "Harga": "Rp180000"
    },
    {
        "Nama": "Wooyoung",
        "Tanggal": "3 Oktober 2024",
        "Paket": "Foto kelas",
        "Harga": "Rp250000"
    },
    {
        "Nama": "Seonghwa",
        "Tanggal": "6 Oktober 2024",
        "Paket": "Foto keluarga",
        "Harga": "Rp300000"
    },
    {
        "Nama": "Hongjoong",
        "Tanggal": "8 Oktober 2024",
        "Paket": "Self photo",
        "Harga": "Rp100000"
    }
]

kesempatan_login = 3

def clear_screen():
    os.system('cls || clear')

def tampilkan_pelanggan(data_pelanggan):
    for index in range(len(data_pelanggan)):
        print(f"Data pelanggan ke-{index+1}")
        print(f"Nama pelanggan: {data_pelanggan[index]['Nama']}")
        print(f"Tanggal booking: {data_pelanggan[index]['Tanggal']}")
        print(f"Paket foto: {data_pelanggan[index]['Paket']}")
        print(f"Total bayar: Rp{data_pelanggan[index]['Harga']}")
        print("=" * 30)

def tambah_pelanggan():
    while True:
        pelanggan_baru = input("Masukkan nama pelanggan baru: ").strip()
        if pelanggan_baru:
            break
        print("Nama pelanggan tidak boleh kosong.")
    
    while True:
        tanggal_baru = input("Masukkan tanggal booking: ").strip()
        if tanggal_baru:
            break
        print("Tanggal booking tidak boleh kosong.")
    
    while True:
        paket_foto = input("Masukkan paket foto: ").strip()
        if paket_foto:
            break
        print("Paket foto tidak boleh kosong.")
    
    while True:
        harga_bayar = input("Masukkan harga paket: ").strip()
        if harga_bayar:
            break
        print("Harga paket tidak boleh kosong.")
    
    pelanggan_baru = {
        "Nama": pelanggan_baru,
        "Tanggal": tanggal_baru,
        "Paket": paket_foto,
        "Harga": harga_bayar
    }
    return pelanggan_baru

def edit_pelanggan(index_edit, data_pelanggan):
    clear_screen()
    if 0 <= index_edit < len(data_pelanggan):
        nama_baru = input("Masukkan nama baru: ")
        tanggal_baru = input("Masukkan tanggal booking baru: ")
        paket_baru = input("Masukkan paket foto baru: ")
        harga_baru = input("Masukkan harga baru: ")

        data_pelanggan[index_edit]["Nama"] = nama_baru or data_pelanggan[index_edit]["Nama"]
        data_pelanggan[index_edit]["Tanggal"] = tanggal_baru or data_pelanggan[index_edit]["Tanggal"]
        data_pelanggan[index_edit]["Paket"] = paket_baru or data_pelanggan[index_edit]["Paket"]
        data_pelanggan[index_edit]["Harga"] = harga_baru or data_pelanggan[index_edit]["Harga"]

        print(f"Data pelanggan atas nama {nama_baru} berhasil diperbarui")
    else:
        print("Nomor pelanggan tidak valid.")

def hapus_pelanggan(index_hapus, daftar_pelanggan):
    if 0 <= index_hapus < len(daftar_pelanggan):
        pelanggan_dihapus = daftar_pelanggan.pop(index_hapus)
        return f"Pelanggan atas nama {pelanggan_dihapus['Nama']} berhasil dihapus."
    else:
        return "Nomor pelanggan tidak valid."

def menu_admin():
    while True:
        print("""
=======================================
                MENU ADMIN
=======================================
1. Lihat data pelanggan
2. Buat data pelanggan baru
3. Perbarui data pelanggan
4. Hapus pelanggan yang sudah selesai
5. Keluar dari program
=======================================""")
        menu = input("Pilih menu: ")
        clear_screen()
        match(menu):
            case "1":
                tampilkan_pelanggan(data_pelanggan)
                input("Tekan enter untuk kembali ke menu...")
                clear_screen()
            case "2":
                pelanggan_baru = tambah_pelanggan()
                data_pelanggan.append(pelanggan_baru)
                print(f"Data pelanggan baru atas nama {pelanggan_baru['Nama']} telah berhasil ditambahkan")
                input("Tekan enter untuk kembali ke menu...")
                clear_screen()
            case "3":
                tampilkan_pelanggan(data_pelanggan)
                index_edit = int(input("Masukkan nomor pelanggan yang ingin diubah: ")) - 1
                edit_pelanggan(index_edit, data_pelanggan)
                input("Tekan enter untuk kembali ke menu...")
                clear_screen()
            case "4":
                tampilkan_pelanggan(data_pelanggan)
                index_hapus = int(input("Masukkan nomor pelanggan yang ingin dihapus: ")) - 1
                hapus = hapus_pelanggan(index_hapus, data_pelanggan)
                print(hapus)
                input("Tekan enter untuk kembali ke menu...")
                clear_screen()
            case "5":
                print("Keluar dari program.")
                exit()
            case _:
                print(f"Menu {menu} tidak tersedia, silahkan pilih menu ulang")
                input("Tekan enter untuk memilih menu lagi...")

def menu_user():
    while True:
        print("""
=======================================
                MENU USER
=======================================
1. Lihat data pelanggan
2. Buat data pelanggan baru
3. Keluar dari program
=======================================""")
        menu = input("Pilih menu: ")
        clear_screen()
        match(menu):
            case "1":
                tampilkan_pelanggan(data_pelanggan)
                input("Tekan enter untuk kembali ke menu...")
                clear_screen()
            case "2":
                pelanggan_baru = tambah_pelanggan()
                data_pelanggan.append(pelanggan_baru)
                print(f"Data pelanggan baru atas nama {pelanggan_baru['Nama']} telah berhasil ditambahkan")
                input("Tekan enter untuk kembali ke menu...")
                clear_screen()
            case "3":
                print("Keluar dari program.")
                exit()
            case _:
                print(f"Menu {menu} tidak tersedia, silahkan pilih menu ulang")
                input("Tekan enter untuk memilih menu lagi...")

def login():
    kesempatan = kesempatan_login
    print("Silakan login terlebih dahulu.")
    while kesempatan > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if username in data_login and data_login[username]['password'] == password:
            print("\nLogin berhasil, selamat datang.")
            input("klik enter untuk melanjutkan")
            clear_screen()
            
            if username == "admin":
                menu_admin()
            else:
                menu_user()
            break
        
        else:
            print("Username atau password salah, silahkan coba lagi")
            kesempatan -= 1
            print(f"Kesempatan tersisa {kesempatan} kali\n")

    if kesempatan == 0:
        print("Kesempatan habis. Program berhenti.")
        exit()

while True:
    print("Silakan login terlebih dahulu.")
    sudah_punya = input("Apakah Anda sudah punya akun? (Ya/Tidak) : ")
    clear_screen()
    if sudah_punya == 'Ya':
        login()
    elif sudah_punya == 'Tidak':
        print("Silahkan buat akun terlebih dahulu")
        username_baru = input("Masukkan username baru: ")
        password_baru = input("Masukkan password baru: ")
        data_login[username_baru] = {
            "username": username_baru,
            "password": password_baru
        }
        print(f"User baru dengan username {username_baru} berhasil ditambahkan.\n")
        input("Klik enter untuk melanjutkan")
        clear_screen()
        continue
    
    else:
        print("Input tidak valid. Masukkan 'Ya' atau 'Tidak'.")
        