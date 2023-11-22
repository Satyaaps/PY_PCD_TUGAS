# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya  (2205551040)
# 2. Ni Komang Gita Sri Adnyani         (2205551010)
# 3. I Putu Nanda Febian Danan Jaya     (2205551093)

# *************************************************************************************

from PIL import Image
import numpy as np

# Baca gambar RGB
img_rgb = np.array(Image.open('foto2.png'))

# Simpan gambar grayscale
Image.fromarray(img_rgb).save('download_grayscale.jpg')

# Konversi gambar grayscale ke gambar biner
threshold = 128
img_binary = np.where(img_rgb >= threshold, 255, 0)

# Simpan gambar biner
Image.fromarray(img_binary.astype(np.uint8)).save('2.binary.jpg')
