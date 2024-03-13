import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_indonesian_flag():
    # Buat figur dan sumbu
    fig, ax = plt.subplots()

    # Tambahkan persegi panjang merah (bagian atas bendera)
    red_rectangle = patches.Rectangle((0, 0.5), 1, 0.5, linewidth=1, edgecolor='none', facecolor='#FF0000')
    ax.add_patch(red_rectangle)

    # Tambahkan persegi panjang putih (bagian bawah bendera)
    white_rectangle = patches.Rectangle((0, 0.3), 1, 0.5, linewidth=1, edgecolor='none', facecolor='#FFFFFF')
    ax.add_patch(white_rectangle)

    blue_rectangle = patches.Rectangle((0, 0 ), 1, 0.5, linewidth=1, edgecolor='none', facecolor='#0000FF') 
    ax.add_patch(blue_rectangle)


    # Atur warna latar belakang menjadi hitam
    fig.patch.set_facecolor('#000000')

    # Atur batas sumbu
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Hilangkan sumbu
    ax.axis('off')

    # Tampilkan bendera
    plt.show()

# Panggil fungsi untuk membuat bendera Indonesia
create_indonesian_flag()
