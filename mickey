print("\033c")
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 10000)
plt.figure(figsize=(8, 9))

# Kepala Mickey Mouse
y_head_upper = 5 + (25 - (x - 5) ** 2) ** 0.5
plt.plot(x, y_head_upper, '-k', label='kepala')
plt.plot(x, 5 - (25 - (x - 5) ** 2) ** 0.5, '-k')

def telinga(t1, t2, radius):
    y_ear_upper = t1 + (radius**2 - (x - t2)**2)**0.5
    y_ear_lower = t1 - (radius**2 - (x - t2)**2)**0.5
    plt.plot(x, y_ear_upper, '-k', label='telinga')
    plt.plot(x, y_ear_lower, '-k')

# Telinga kiri
telinga(5 + 2 * np.sqrt(5), 3, 2)

# Telinga kanan
telinga(5 + 2 * np.sqrt(5), 7, 2)

plt.legend(loc='upper center')
plt.grid()
plt.show()
