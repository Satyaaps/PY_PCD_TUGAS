import cv2
import numpy as np

# Fungsi untuk mengambil nilai piksel dari citra dengan penanganan batas
def get_pixel_value(image, i, j):
    m, n = image.shape
    if i < 0:
        i = 0
    elif i >= m:
        i = m - 1
    if j < 0:
        j = 0
    elif j >= n:
        j = n - 1
    return image[i, j]

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

# Fungsi untuk mengaplikasikan efek emboss pada citra
def emboss_effect(image):
    m, n = image.shape

    # Kernel untuk efek emboss
    kernel = np.array([[-2, -1, 0],
                       [-1,  1, 1],
                       [0,  1, 2]])

    # Lakukan konvolusi dengan kernel efek emboss
    embossed_image = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            embossed_image[i, j] = np.sum(kernel * get_pixel_value(image, i-1, j-1))

    # Normalisasi nilai pixel ke rentang 0-255
    embossed_image = np.clip(embossed_image, 0, 255)

    return embossed_image.astype(np.uint8)

# Baca citra
image = cv2.imread('TUGAS_3/asset/foto2.jpg', cv2.IMREAD_GRAYSCALE)

# Aplikasikan efek emboss
embossed_image = emboss_effect(image)

# Tampilkan citra asli dan citra dengan efek emboss
cv2.imshow('Original Image', image)
cv2.imshow('Embossed Image', embossed_image)

# Tunggu pengguna menekan tombol apa pun sebelum menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()