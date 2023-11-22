import cv2
import numpy as np

# Fungsi untuk melakukan konvolusi pada citra dengan kernel tertentu
def convolution(image, kernel):
    m, n = image.shape
    k_m, k_n = kernel.shape
    pad_size = k_m // 2

    # Buat citra dengan padding
    padded_image = np.pad(image, pad_size, mode='constant')

    # Inisialisasi citra hasil konvolusi
    result = np.zeros((m, n))

    # Lakukan operasi konvolusi
    for i in range(m):
        for j in range(n):
            result[i, j] = np.sum(padded_image[i:i+k_m, j:j+k_n] * kernel)

    return result

# Fungsi untuk melakukan penghalusan citra dengan Gaussian blur
def gaussian_blur(image, ksize):
    sigma = 1.4  # Ganti dengan nilai sigma yang diinginkan
    kernel = np.fromfunction(
        lambda x, y: (1/(2*np.pi*sigma**2)) * np.exp(-((x-(ksize-1)//2)**2 + (y-(ksize-1)//2)**2)/(2*sigma**2)),
        (ksize, ksize)
    )
    kernel = kernel / np.sum(kernel)  # Normalisasi kernel

    # Lakukan konvolusi dengan kernel Gaussian
    smoothed_image = convolution(image, kernel)

    return smoothed_image

# Baca citra
image = cv2.imread('TUGAS_3/asset/noise_1.png', cv2.IMREAD_GRAYSCALE)

# Aplikasikan Gaussian blur dengan kernel 5x5
ksize = 5
smoothed_image = gaussian_blur(image, ksize)

# Tampilkan citra asli dan citra hasil penghalusan
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image.astype(np.uint8))  # Konversi tipe data kembali ke uint8

# Tunggu pengguna menekan tombol apa pun sebelum menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
