# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya (2205551040)
# 2. Ni Komang Gita Sri Adnyani (2205551010)
# 3. I Putu Nanda Febian Danan Jaya (2205551093)

# *************************************************************************************


import cv2 # Mengimpor library OpenCV untuk membaca, menulis, dan memanipulasi gambar.
import numpy as np # Mengimpor library NumPy untuk melakukan operasi numerik pada array.
import matplotlib.pyplot as plt # Mengimpor library Matplotlib untuk membuat plot.

# Definisi fungsi process_image() yang mengambil dua argumen: path ke file gambar dan path ke file teks keluaran. Fungsi ini memproses gambar dan menghasilkan file teks yang berisi informasi RGB dan intensitas setiap piksel dalam gambar.
def process_image(image_path, output_file): 
    # Blok kode yang akan dijalankan jika tidak ada kesalahan.
    try: 
        # Membaca gambar dari file.
        image = cv2.imread(image_path) 

        # Memeriksa apakah gambar berhasil dibaca. Jika tidak, fungsi akan mengembalikan kesalahan.
        if image is None: 
            raise FileNotFoundError(f"File '{image_path}' not found.")

        # Mendapatkan dimensi gambar.
        height, width, _ = image.shape 

        # Mengubah gambar menjadi citra grayscale.
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

        # Menghitung histogram gambar.
        hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

        # Open the output file for writing
        with open(output_file, 'w') as file: # digunakan untuk membuka file teks keluaran untuk menulis.
            # Output RGB values and coordinates of each pixel
            for y in range(height): # digunakan untuk melakukan iterasi melalui setiap piksel dalam gambar.
                for x in range(width):
                    intensity = gray_image[y, x] # digunakan untuk mendapatkan intensitas warna dari piksel saat ini.
                    b, g, r = image[y, x]  # digunakan untuk mendapatkan nilai merah, hijau, dan biru dari piksel saat ini.
                    file.write(f"({x},{y}) => RGB Value: ({r},{g},{b}), Color Intensity: {intensity}\n") # digunakan untuk menulis informasi RGB dan intensitas piksel saat ini ke file teks keluaran

        # Menampilkan Histogram
        plt.figure(figsize=(8, 6))
        plt.title('Grayscale Image Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.plot(hist)
        plt.xlim([0, 256])
        plt.grid(True)
        plt.show()

        # Menampilkan Original Image
        cv2.imshow('Original Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print(f"Output saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Menetapkan path ke file gambar yang akan diproses.
    image_path = 'foto1.png'
    # Output nama file
    output_file = '1.Image_Info.txt'
    process_image(image_path, output_file)
