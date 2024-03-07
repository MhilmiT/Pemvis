# Program Python yang melibatkan data berjenis set untuk otomotif

# Membuat set
car_brands = {"Toyota", "Honda", "Ford", "Chevrolet"}
motorcycle_brands = {"Harley-Davidson", "Yamaha", "Suzuki", "Ducati"}

# Menampilkan isi set
print("Merek Mobil:", car_brands)
print("Merek Motor:", motorcycle_brands)

# Menambahkan merek ke dalam set
car_brands.add("Tesla")
motorcycle_brands.add("Kawasaki")

# Menampilkan set setelah penambahan
print("\nSetelah penambahan:")
print("Merek Mobil:", car_brands)
print("Merek Motor:", motorcycle_brands)

# Menghapus merek dari set
car_brands.remove("Chevrolet")
motorcycle_brands.discard("Ducati")

# Menampilkan set setelah penghapusan
print("\nSetelah penghapusan:")
print("Merek Mobil:", car_brands)
print("Merek Motor:", motorcycle_brands)

# Operasi set lainnya
common_brands = car_brands.intersection(motorcycle_brands)
all_brands = car_brands.union(motorcycle_brands)

# Menampilkan hasil operasi set
print("\nMerek yang sama di antara mobil dan motor:", common_brands)
print("Semua merek (gabungan) dari mobil dan motor:", all_brands)
