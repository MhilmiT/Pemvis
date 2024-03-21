es_buah = set()

print("MEMBUAT ES BUAH")

buah_1 = input("Masukkan nama buah pertama: ")
buah_2 = input("Masukkan nama buah kedua: ")
buah_3 = input("Masukkan nama buah ketiga: ")

es_buah.add(buah_1)
es_buah.add(buah_2)
es_buah.add(buah_3)

print("Buah-buahan telah ditambahkan ke dalam es buah.")

print("Isi dari Es Buah:")
for buah in es_buah:
    print("-", buah)

print("Jumlah buah dalam es buah:", len(es_buah))

hapus_buah = input("Masukkan nama buah yang ingin dikeluarkan: ")
if hapus_buah in es_buah:
    es_buah.remove(hapus_buah)
    print(f"{hapus_buah} telah dikeluarkan dari es buah.")
else:
    print(f"{hapus_buah} tidak ada dalam es buah.")

print("Isi dari Es Buah:")
for buah in es_buah:
    print("-", buah)
