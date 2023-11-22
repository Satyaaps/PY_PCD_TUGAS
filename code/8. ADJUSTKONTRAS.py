# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya  (2205551040)
# 2. Ni Komang Gita Sri Adnyani         (2205551010)
# 3. I Putu Nanda Febian Danan Jaya     (2205551093)

# *************************************************************************************


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image):
    width, height = image.size
    histogram = np.zeros(256)

    for y in range(height):
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            histogram[pixel_value] += 1

    return histogram

def adjust_contrast(image, contrast_factor):
    if contrast_factor <= 0:
        print("Faktor kontras harus lebih besar dari 0.")
        return

    width, height = image.size
    image = image.convert('L')  # Mengubah gambar ke mode 'L' (grayscale)
    result_img = Image.new('L', (width, height))

    for y in range(height):
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            new_pixel_value = int(pixel_value * contrast_factor)
            new_pixel_value = max(0, min(new_pixel_value, 255))
            result_img.putpixel((x, y), new_pixel_value)

    result_img.show()

    original_histogram = calculate_histogram(image)
    adjusted_histogram = calculate_histogram(result_img)

    plt.figure(figsize=(12, 6))

    plt.subplot(221)
    plt.imshow(image, cmap='gray')
    plt.title('Gambar Asli')
    plt.axis('off')

    plt.subplot(222)
    plt.bar(range(256), original_histogram, width=0.7, color='black')
    plt.title('Histogram Sebelum')

    plt.subplot(223)
    plt.imshow(result_img, cmap='gray')
    plt.title('Gambar Sesudah')
    plt.axis('off')

    plt.subplot(224)
    plt.bar(range(256), adjusted_histogram, width=0.7, color='black')
    plt.title('Histogram Sesudah')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    image_path = "foto1.png"

    try:
        contrast_factor = float(input("Masukkan faktor kontras: "))
        if contrast_factor <= 0:
            print("Faktor kontras harus lebih besar dari 0.")
        else:
            img = Image.open(image_path)
            adjust_contrast(img, contrast_factor)
    except ValueError:
        print("Faktor kontras harus berupa angka.")
