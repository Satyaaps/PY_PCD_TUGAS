# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya (2205551040)
# 2. Ni Komang Gita Sri Adnyani (2205551010)
# 3. I Putu Nanda Febian Danan Jaya (2205551093)

# *************************************************************************************

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
image = cv2.imread('foto1.jpg')

# Menghitung tinggi (h) dan lebar (w) gambar
h, w = image.shape[:2]

# Inisialisasi gambar hasil pencerminan
horizontal_mirror = np.copy(image)
vertical_mirror = np.copy(image)
combined_mirror = np.copy(image)

# Pencerminan Horisontal
for y in range(h):
    for x in range(w):
        horizontal_mirror[y, x] = image[y, w - 1 - x]

# Pencerminan Vertikal
for y in range(h):
    for x in range(w):
        vertical_mirror[y, x] = image[h - 1 - y, x]

# Pencerminan Kombinasi
for y in range(h):
    for x in range(w):
        combined_mirror[y, x] = image[h - 1 - y, w - 1 - x]

# Menampilkan gambar asli dan hasil pencerminan menggunakan matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 4, 1)
plt.title('Gambar Asli')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 4, 2)
plt.title('Pencerminan Horisontal')
plt.imshow(cv2.cvtColor(horizontal_mirror, cv2.COLOR_BGR2RGB))

plt.subplot(1, 4, 3)
plt.title('Pencerminan Vertikal')
plt.imshow(cv2.cvtColor(vertical_mirror, cv2.COLOR_BGR2RGB))

plt.subplot(1, 4, 4)
plt.title('Pencerminan Kombinasi')
plt.imshow(cv2.cvtColor(combined_mirror, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()
