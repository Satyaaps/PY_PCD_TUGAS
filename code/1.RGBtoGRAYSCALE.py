# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya  (2205551040)
# 2. Ni Komang Gita Sri Adnyani         (2205551010)
# 3. I Putu Nanda Febian Danan Jaya     (2205551093)

# *************************************************************************************

from PIL import Image

# Import library yang dibutuhkan
import numpy as np

# Baca gambar RGB
img_rgb = np.array(Image.open('foto1.png'))

# Konversi RGB ke grayscale
ar = 0.2989
ag = 0.5870
ab = 0.1140
img_grayscale = np.zeros_like(img_rgb)
for i in range(img_rgb.shape[0]):
    for j in range(img_rgb.shape[1]):
        r, g, b = img_rgb[i, j]
        img_grayscale[i, j] = ar * r + ag * g + ab * b
print(img_grayscale[0,0])
# Simpan gambar grayscale
Image.fromarray(img_grayscale).save('1.grayscale.jpg')
