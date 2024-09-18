nama = str(input("Masukkan nama "))
nim = int(input("Masukkan NIM "))
umur = int(input("Masukkan umur "))
asal_kota = str(input("Masukkan asal kota "))
tinggi_badan = float(input("Masukkan tinggi badan "))
berat_badan = float(input("Masukkan berat badan "))
jenis_kelamin = str(input("Masukkan jenis kelamin "))
status_mahasiswa = bool(input("Apakah anda mahasiswa aktif?(true/false) "))

biodata = (
    f"====================================\n"
    f"        Biodata Diri\n"
    f"====================================\n"
    f"Nama              : {nama}\n"
    f"NIM               : {nim}\n"
    f"Asal Kota         : {asal_kota}\n"
    f"Umur              : {umur}\n"
    f"Tinggi Badan      : {tinggi_badan} cm\n"
    f"Berat Badan       : {berat_badan} kg\n"
    f"Jenis Kelamin     : {jenis_kelamin}\n"
    f"Status Mahasiswa  : {'Aktif' if status_mahasiswa else 'Tidak aktif'}\n"
    f"====================================\n"
)

total_int = nim+umur
total_float = tinggi_badan+berat_badan

print(f"{biodata}\nTotal variabel integer: {total_int}\nTotal variabel float: {total_float}")