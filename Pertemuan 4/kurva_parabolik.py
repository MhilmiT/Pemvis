print("\033c")
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 10000)

plt.plot(x, (0.01 - x ** 2) ** 0.5, '-k')
plt.plot(x, -(0.01 - x ** 2) ** 0.5, '-k')  # Perubahan tanda untuk menggambar bagian bawah lingkaran

y = x - x - 0
y1 = x ** 3 - 2 * x ** 2 - 5 * x + 6

plt.plot(x, y, '-k')

plt.plot(x, y1, '-r', label='y1')

plt.legend(loc='upper left')  # Perubahan lokasi legenda agar sesuai
plt.grid()
plt.show()
