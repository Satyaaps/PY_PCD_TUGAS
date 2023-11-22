# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya  (2205551040)
# 2. Ni Komang Gita Sri Adnyani         (2205551010)
# 3. I Putu Nanda Febian Danan Jaya     (2205551093)

# *************************************************************************************

from PIL import Image

# Baca gambar RGB
img_rgb = Image.open('foto2.png')

# Konversi RGB ke grayscale
img_grayscale = img_rgb.convert('L')

# Simpan gambar grayscale
img_grayscale.save('grayscale_image.jpg')

# Konversi gambar grayscale ke gambar M-Bit dengan resolusi tertentu
for bit_resolution in [1, 2, 3]:
    width, height = img_grayscale.size
    mbit_img = Image.new('1', (width, height), 0)  # '1' mengindikasikan gambar biner (mode 1)
    for y in range(height):
        for x in range(width):
            gray_value = img_grayscale.getpixel((x, y))
            mbit_value = int(gray_value / (256 / (2**bit_resolution)))
            mbit_img.putpixel((x, y), mbit_value)
    mbit_img.save(f'3.mbit_image_{bit_resolution}bit.png')
