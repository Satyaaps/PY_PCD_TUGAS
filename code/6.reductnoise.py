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

# Fungsi untuk mengurangi noise dengan filter rata-rata
def reduce_noise(image, kernel_size):
    # Buat kernel filter rata-rata
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)

    # Lakukan konvolusi dengan kernel filter rata-rata
    denoised_image = convolution(image.astype(float), kernel)

    # Normalisasi nilai pixel ke rentang 0-255
    denoised_image = np.clip(denoised_image, 0, 255)

    return denoised_image.astype(np.uint8)

# Baca citra
image = cv2.imread('TUGAS_3/asset/noise_3.jpg', cv2.IMREAD_GRAYSCALE)

# Aplikasikan pengurangan noise dengan filter rata-rata
denoised_image = reduce_noise(image, 5)  # Ganti nilai kernel_size sesuai kebutuhan

# Tampilkan citra asli dan citra hasil reduksi noise
cv2.imshow('Original Image', image)
cv2.imshow('Denoised Image', denoised_image)

# Tunggu pengguna menekan tombol apa pun sebelum menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
