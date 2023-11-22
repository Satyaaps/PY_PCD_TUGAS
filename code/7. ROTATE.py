# # ANGGOTA KELOMPOK : 
# # 1. I Gede Satya Ariya Putra Sangjaya (2205551040)
# # 2. Ni Komang Gita Sri Adnyani (2205551010)
# # 3. I Putu Nanda Febian Danan Jaya (2205551093)

# # *************************************************************************************


# from PIL import Image

# # Buka gambar
# gambar_input = input("Masukkan nama file gambar: ")
# img = Image.open(gambar_input)

# # Minta pengguna untuk memasukkan sudut rotasi
# sudut_rotasi = float(input("Masukkan sudut rotasi (misalnya 90 untuk searah jarum jam, -90 untuk berlawanan arah jarum jam): "))

# # Rotasi gambar sesuai dengan masukan pengguna
# img_rotated = img.rotate(sudut_rotasi)

# # Simpan gambar yang sudah dirotasi
# gambar_output = input("Masukkan nama file untuk menyimpan gambar yang sudah dirotasi: ")
# img_rotated.save(gambar_output)

# # Tampilkan gambar yang sudah dirotasi
# img_rotated.show()


from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Buka gambar
gambar_input = "foto1.png"
img = Image.open(gambar_input)

# Daftar sudut rotasi yang akan digunakan
sudut_rotasi = [0, 90, 180, 270, 360]

# Membuat subplot Matplotlib untuk menampilkan gambar-gambar yang sudah dirotasi
fig, axes = plt.subplots(1, len(sudut_rotasi), figsize=(15, 3))

for i, sudut in enumerate(sudut_rotasi):
    # Rotasi gambar sesuai sudut
    img_rotated = img.rotate(sudut)
    
    # Mengkonversi gambar PIL ke array NumPy
    img_array = np.array(img_rotated)
    
    # Menampilkan gambar menggunakan Matplotlib
    axes[i].imshow(img_array)
    axes[i].set_title(f'{sudut}°')
    axes[i].axis('off')

plt.show()
