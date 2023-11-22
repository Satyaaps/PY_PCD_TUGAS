import cv2
import matplotlib.pyplot as plt

# Baca citra dan konversi ke citra grayscale
image = cv2.imread('TUGAS_3/asset/clear_3.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Menerapkan filter Canny
filter_canny = cv2.Canny(gray_image, 25, 255, L2gradient=False)

# Menerapkan filter Sobel
filter_sobel = cv2.Sobel(src=gray_image, ddepth=cv2.CV_8U, dx=1, dy=1, ksize=5)

# Menampilkan citra asli, hasil filter Canny, dan hasil filter Sobel di dalam satu gambar
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(filter_canny, cmap='gray')
plt.title('Canny Filter')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(filter_sobel, cmap='gray')
plt.title('Sobel Filter')
plt.axis('off')

plt.show()
