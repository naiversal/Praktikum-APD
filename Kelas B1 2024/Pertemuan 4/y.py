#for i in range(6):
#    for i in range(6):
#        print("*", end="")
#    print()

#for i in range(6):
#    print("*", end == " ")


kesempatan = 3
while kesempatan > 0:
    username = input("masukkan username: ")
    password = input("masukkan password: ")

    if username == "admin" and password == "admin#1234":
        print("berhasil login")
        break
    else:
        print("username atau password salah")
        kesempatan -= 1
        print(f"kesempatan tersisa {kesempatan} kali")
        
print("program utama")