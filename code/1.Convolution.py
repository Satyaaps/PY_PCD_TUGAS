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

# Fungsi untuk melakukan konvolusi pada citra
def convolution(image, kernel):
    return convolve(image, kernel, mode='constant', cval=0.0)

# Fungsi untuk menampilkan citra
def show_image(image, title):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Menggunakan citra dari file
image_path = 'TUGAS_3/asset/foto2.jpg'  # Ganti dengan path gambar Anda
image = read_and_show_image(image_path, 'Original Image')

# Membuat kernel contoh
kernel = np.array([[0, -1, 0],
                   [-2, 3, -2],
                   [0, -1, 0]])

# Melakukan konvolusi pada citra dengan kernel yang telah dibuat
result = convolution(image, kernel)

# Menampilkan citra asli dan hasil konvolusi
show_image(image, 'Original Image')
show_image(result, 'Convolution Result')

print('Real : \n', image)
print('Convolution : \n', result)
