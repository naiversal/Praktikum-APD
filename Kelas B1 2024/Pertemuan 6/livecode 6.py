data_mhs = [
    {
    "nama" : "budi",
    "role" : "admin",
    "username" : "BudiAsli",
    "password" : "pecelleleturbo"
    },

    {
    "nama" : "supri",
    "role" : "user"
    },
]

print(data_mhs[0]['nama'])

data_mhs2 = [
    ["budi", "admin"],
    ["supri", "user"]
]

print(data_mhs2[0][1])

# data_mhs = {
#     "nama" : "chasca",
#     "nim" : 68,
#     "matkul" : ["apd", "kalkulus", "jarkom"],
#     "dosen" : {
#         "nama" : "pak awang",
#         "matkul" : "apd"
#     }
# }

# print(data_mhs['dosen']['nama'])

# for value in data_mhs.values():
#     print(value)

# print(len(data_mhs))

# del data_mhs["nim"]

# cache = data_mhs.pop('nim')

# print(data_mhs, "Dictionary")
# print(cache, "Cache")

# data_mhs["id"] = cache
# print(data_mhs)

# print(data_mhs.clear(), "Clear")
# print(data_mhs['nama'])
# print(data_mhs['nim'])
# print(data_mhs)

# print(data_mhs['mapel'])
# print(data_mhs.get('mapel', 'gada'))

# for data in data_mhs:
#     print(data)

# for key_data, value_data in data_mhs.items():
#     print(f"Key: {key_data}\nValue: {value_data}\n)

# data_mhs['alamat'] = "Samarinda"
# data_mhs['alamat'] = "Tenggarong"

# data_mhs.update({"alamat" : "Samarinda"})
# print(data_mhs)

# data_mhs["nama"] = "xilonen"

# key = "apel", "jeruk", "mangga", "semangka", "anggur"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# nilai = {

#     "mtk" : 80,
#     "b.indo" : 90,
#     "b. ing" : 81,
#     "kimia" : 20
# }

# print("nilai : ", nilai.setdefault("kimia", 70))
# print("")

# print(nilai)