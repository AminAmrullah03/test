# Impor modul matplotlib untuk menggambar flow graph
import matplotlib.pyplot as plt

# Definisi simpul-simpul dalam flow graph
simpul_awal = "Mulai"
simpul_1 = "Pernyataan 1"
simpul_2 = "Pernyataan 2"
simpul_keputusan = "Titik Keputusan"
simpul_3 = "Pernyataan 3"
simpul_akhir = "Selesai"

# Menggambar flow graph
plt.figure(figsize=(8, 6))

# Menghubungkan simpul-simpul dengan edge
plt.plot([simpul_awal, simpul_1], [1, 1], 'ro-')
plt.plot([simpul_1, simpul_2], [1, 2], 'ro-')
plt.plot([simpul_2, simpul_keputusan], [2, 3], 'ro-')
plt.plot([simpul_keputusan, simpul_3], [3, 4], 'ro-')
plt.plot([simpul_keputusan, simpul_akhir], [3, 5], 'ro-')

# Menambahkan label ke simpul-simpul
plt.text(simpul_awal, 1, simpul_awal, fontsize=12, ha='right')
plt.text(simpul_1, 1, simpul_1, fontsize=12, ha='right')
plt.text(simpul_2, 2, simpul_2, fontsize=12, ha='right')
plt.text(simpul_keputusan, 3, simpul_keputusan, fontsize=12, ha='right')
plt.text(simpul_3, 4, simpul_3, fontsize=12, ha='right')
plt.text(simpul_akhir, 5, simpul_akhir, fontsize=12, ha='right')

# Menambahkan label ke edge
plt.text(simpul_1, 1.5, "True", fontsize=10, ha='center')
plt.text(simpul_2, 2.5, "True", fontsize=10, ha='center')
plt.text(simpul_keputusan, 3.5, "False", fontsize=10, ha='center')

# Menyembunyikan sumbu x dan y
plt.axis('off')

# Menampilkan flow graph
plt.show()
