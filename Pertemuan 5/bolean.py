#Case 1
print("Case 1")
#Data bertipe Boolean yang Kita Deklarasikan (Cara Standar)
f = bool(True)
g = bool (False)
print(f)
print(g)
print("=======================================")

#Case 2
print("Case 2")
#Data Bertipe Boolean Dalam Berbagai Konteks
#Tercatat Dengan Sendirinya oleh Komputer tanpa Deklarasi.
print(3>2)
print(3+2==5)
print (3<2)
print("=======================================")

#Case 3
print("Case 3")
#Data Bertipe Boolean Dalam Berbagai Konteks
#Tercatat Dengan Sendirinya oleh Komputer tanpa Deklarasi.
Penghasilan= 20000000
PenghasilanTanpaPajak = 4000000
if Penghasilan <= PenghasilanTanpaPajak:
  PajakYangHarusDibayar = 0

if Penghasilan > PenghasilanTanpaPajak:
  PajakYangHarusDibayar = 0.1 * Penghasilan
print("Pajak yang harus Anda bayar: Rp ", PajakYangHarusDibayar)