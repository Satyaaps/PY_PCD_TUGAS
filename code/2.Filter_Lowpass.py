# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya  (2205551040)
# 2. Ni Komang Gita Sri Adnyani         (2205551010)
# 3. I Putu Nanda Febian Danan Jaya     (2205551093)

# *************************************************************************************
 
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Fungsi untuk membaca dan menampilkan gambar
def read_and_show_image(image_path, title):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()
    return image

# Fungsi untuk menerapkan filter lowpass pada citra
def apply_lowpass_filter(image, filter_size):
    # Membuat filter rata-rata dengan ukuran yang ditentukan
    kernel = np.ones((filter_size, filter_size)) / filter_size**2
    
    # Melakukan konvolusi dengan filter rata-rata
    return convolve(image, kernel, mode='constant', cval=0.0)

# Fungsi untuk menampilkan citra
def show_image(image, title):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Menggunakan citra dari file
image_path = 'TUGAS_3/asset/noise_2.jpeg'  # Ganti dengan path gambar Anda
image = read_and_show_image(image_path, 'Original Image')

# Menentukan ukuran filter lowpass (harus berupa bilangan ganjil)
filter_size = 3

# Menerapkan filter lowpass pada citra
result = apply_lowpass_filter(image, filter_size)

# Menampilkan citra asli dan hasil filter lowpass
show_image(image, 'Original Image')
show_image(result, f'Lowpass Filter Result (Size: {filter_size})')

# Menampilkan array dari koordinat citra
print('Real : \n', image)
print('Filter Result : \n', result)
