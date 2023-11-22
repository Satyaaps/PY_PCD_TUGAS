# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya  (2205551040)
# 2. Ni Komang Gita Sri Adnyani         (2205551010)
# 3. I Putu Nanda Febian Danan Jaya     (2205551093)

# *************************************************************************************


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def adjust_brightness(image_path, output_path, brightness_factor):
    # Buka gambar menggunakan PIL
    image = Image.open(image_path)

    # Konversi gambar ke mode 'L' (grayscale) jika belum
    if image.mode != 'L':
        image = image.convert('L')

    # Konversi gambar menjadi numpy array
    img_array = np.array(image)

    # Menghitung gambar dengan penambahan kecerahan (brightness)
    img_brightness = img_array + brightness_factor

    # Membatasi nilai piksel dalam rentang 0-255
    img_brightness = np.clip(img_brightness, 0, 255)

    # Simpan gambar yang telah diubah kecerahannya
    img_brightness = Image.fromarray(img_brightness.astype('uint8'))
    img_brightness.save(output_path)

    # Hitung histogram gambar
    hist = img_brightness.histogram()

    # Tampilkan gambar dan histogram dalam satu figure
    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 2, 1)
    plt.title('Gambar Kecerahan')
    plt.imshow(img_brightness, cmap='gray')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title('Histogram Gambar Kecerahan')
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Frekuensi')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    input_image_path = 'foto5.png'
    output_image_path = 'gambar_kecerahan.jpg'
    brightness_factor = 2  # Ganti dengan nilai positif atau negatif sesuai kebutuhan
    adjust_brightness(input_image_path, output_image_path, brightness_factor)
