# ANGGOTA KELOMPOK :
# 1. I Gede Satya Ariya Putra Sangjaya  (2205551040)
# 2. Ni Komang Gita Sri Adnyani         (2205551010)
# 3. I Putu Nanda Febian Danan Jaya     (2205551093)

# *************************************************************************************

import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = plt.imread("foto4.jpg").astype(np.uint8)

if len(image.shape) == 3:
    image = np.mean(image, axis=2).astype(np.uint8)

# Calculate the histogram
nx, ny = image.shape
total_pixels = nx * ny
histogram = np.zeros(256, dtype=int)
for pixel_value in image.flat:
    histogram[pixel_value] += 1

# Calculate the cumulative distribution function (CDF)
cdf = np.cumsum(histogram)
cdf = 255 * cdf / total_pixels

# Equalize the image
equalized_image = cdf[image]

# Display the original and equalized images along with their histograms
plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap="gray")
plt.title("Equalized Image")

plt.subplot(2, 2, 3)
plt.hist(image.ravel(), 256, [0, 255])
plt.title("Original Histogram")

plt.subplot(2, 2, 4)
plt.hist(equalized_image.ravel(), 256, [0, 255])
plt.title("Equalized Histogram")

plt.show()
