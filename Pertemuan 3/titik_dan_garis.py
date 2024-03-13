print("\033c")  # To clear the console

import numpy as np
import matplotlib.pyplot as plt

# User informs the coordinates of the two points for the line.
y1 = 600
x1 = 200
y2 = 200
x2 = 600

# User decides the points' (vertex) diameter and color
pd = int(6)
pr = 255
pg = 255
pb = 0

# User decides the line width and color
lw = int(6)
lr = 255
lg = 255
lb = 0

# Setting the size of the canvas
col = int(800)
row = int(800)
print('col, row =', col, ',', row)


# FUNCTION TO DRAW A LINE
def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)  # Preparing the black canvas
    hd = int(pd / 2)  # Calculate the half point diameter.
    hw = int(lw / 2)  # Calculate the half line width.
    dy = y2 - y1
    dx = x2 - x1

    # Draw the first point.
    for i in range(x1 - hd, x1 + hd + 1):
        for j in range(y1 - hd, y1 + hd + 1):
            if (i - x1) ** 2 + (j - y1) ** 2 <= hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Draw the second point.
    for i in range(x2 - hd, x2 + hd + 1):
        for j in range(y2 - hd, y2 + hd + 1):
            if (i - x2) ** 2 + (j - y2) ** 2 <= hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Draw the line
    if abs(dy) <= abs(dx):
        my = dy / dx
        for i in range(min(x1, x2), max(x1, x2) + 1):
            j = int(my * (i - x1) + y1)
            x = i
            y = j
            for i in range(x - hw, x + hw + 1):
                for j in range(y - hw, y + hw + 1):
                    if (i - x) ** 2 + (j - y) ** 2 <= hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    # Draw the line for lines that tend to be vertical
    if abs(dy) > abs(dx):
        mx = dx / dy
        for j in range(min(y1, y2), max(y1, y2) + 1):
            i = int(mx * (j - y1) + x1)
            x = i
            y = j
            for i in range(x - hw, x + hw + 1):
                for j in range(y - hw, y + hw + 1):
                    if (i - x) ** 2 + (j - y) ** 2 <= hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    return Gambar

# Main Program
hasil = buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()
