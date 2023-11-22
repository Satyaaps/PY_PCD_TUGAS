# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya  (2205551040)
# 2. Ni Komang Gita Sri Adnyani         (2205551010)
# 3. I Putu Nanda Febian Danan Jaya     (2205551093)

# *************************************************************************************
 
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter

# Fungsi untuk membaca dan menampilkan gambar
def read_and_show_image(image_path, title):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()
    return image

# Fungsi untuk menerapkan filter median pada citra
def apply_median_filter(image, size):
    return median_filter(image, size=size)

# Fungsi untuk menampilkan citra
def show_image(image, title):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Menggunakan citra dari file
image_path = 'TUGAS_3/asset/noise_1.png'  # Ganti dengan path gambar Anda
image = read_and_show_image(image_path, 'Original Image')

# Menentukan ukuran filter median (harus berupa bilangan ganjil)
filter_size = 5

# Menerapkan filter median pada citra
result = apply_median_filter(image, size=filter_size)

# Menampilkan citra asli dan hasil filter median
show_image(image, 'Original Image')
show_image(result, f'Median Filter Result (Size: {filter_size})')

# Menampilkan array dari koordinat citra
print('Real : \n', image)
print('Filter Result : \n', result)
