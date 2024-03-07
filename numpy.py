import numpy as np

A = np.array(['INF', 'SIF', 'TSP'])
B = np.array([-3, 0, 4, 7])
new_B = B.astype('int32')  # Menggunakan 'int32' daripada 'I'
print(new_B.dtype)

C = np.array([-3, 0, 4, 7])
new_C = C.astype(bool)  # Menggunakan 'C' daripada 'B'
print(new_C.dtype)

# Anda perlu mendefinisikan 'row' dan 'col' sebelum membuat Gambar
row, col = 3, 3
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint16)
Gambar_new = np.uint8(Gambar)

print(Gambar_new.dtype)
