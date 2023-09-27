# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya (2205551040)
# 2. Ni Komang Gita Sri Adnyani (2205551010)
# 3. I Putu Nanda Febian Danan Jaya (2205551093)

# *************************************************************************************

import cv2
import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.filedialog import askopenfile

root = Tk()
root.title("Pengolahan Citra Digital")
imgconvert = None
imageinput = None

ukurangambar = (300, 400)
gambarmasuk, copygambar, converting = dict(), dict(), dict()

def box():
    global imgconvert
    if imageinput:
        imgconvert = Image.new("RGB", (imageinput.width, imageinput.height))
        converting["image"] = ImageTk.PhotoImage(imgconvert)
        labelconvert = Label(root, image=converting["image"])
        labelcopy = Label(root, image=converting["image"])
        labelinsert = Label(root, image=converting["image"])
        labelinsert.grid(row=1, column=1)
        labelcopy.grid(row=1, column=2)
        labelconvert.grid(row=1, column=3)
    else:
        messagebox.showerror("Error", "Tidak ada gambar yang diunggah atau gambar belum diubah.")


box()

def tampilkan_histogram_rgb():
    if imgconvert:
        # Ubah gambar menjadi mode RGB jika belum dalam mode tersebut
        if imgconvert.mode != "RGB":
            imgconvert = imgconvert.convert("RGB")
        
        # Hitung histogram gambar RGB
        histogram_r = cv2.calcHist([np.array(imgconvert)[:, :, 0]], [0], None, [256], [0, 256])
        histogram_g = cv2.calcHist([np.array(imgconvert)[:, :, 1]], [0], None, [256], [0, 256])
        histogram_b = cv2.calcHist([np.array(imgconvert)[:, :, 2]], [0], None, [256], [0, 256])

        # Menampilkan histogram
        plt.figure()
        plt.title("Histogram Gambar RGB")
        plt.xlabel("Intensitas Pixel")
        plt.ylabel("Frekuensi")
        plt.plot(histogram_r, color='red', label='Merah')
        plt.plot(histogram_g, color='green', label='Hijau')
        plt.plot(histogram_b, color='blue', label='Biru')
        plt.xlim([0, 256])
        plt.legend()
        plt.show()

def openimage():
    global imageinput
    global imgconvert
    root.imagefile = filedialog.askopenfilename(initialdir="", filetypes=(("png files", "*.png *.jpg *.jpeg"), ("all files", "*.*")))
    fileadress = root.imagefile
    imageinput = Image.open(fileadress).resize(ukurangambar)

    # Konversi gambar ke mode "RGB" jika tidak sudah dalam mode tersebut
    if imageinput.mode != "RGB":
        imageinput = imageinput.convert("RGB")

    imgconvert = imageinput.copy()
    gambarmasuk["image"] = ImageTk.PhotoImage(imageinput)
    tombolInputGambar = Label(root, image=gambarmasuk["image"])
    tombolInputGambar.grid(row=1, column=1)
    
    # Setelah gambar dimuat, tampilkan informasi gambar dan histogram RGB
    tampilkan_informasi_gambar()
    tampilkan_histogram_rgb()
    
def tampilkan_informasi_gambar():
    if imageinput:
        tinggi, lebar = imageinput.size
        resolusi = (lebar, tinggi)
        kedalaman_warna = imageinput.mode
        mode_warna = "Grayscale" if imageinput.mode == "L" else "RGB"  # Mode Grayscale jika gambar awalnya Grayscale, jika tidak, mode RGB

        informasi_text = f"Resolusi: {resolusi}\nKedalaman Warna: {kedalaman_warna}\nMode Warna: {mode_warna}"
        
        informasi_label.config(text=informasi_text)


def copyimage():
    global imgconvert
    global warna

    if imgconvert is None:
        imgconvert = Image.new("RGB", ukurangambar)

    warna = []

    imgcopy = imgconvert.copy()  # Salin gambar dari imgconvert agar mode warnanya juga disalin
    warnafoto = imgcopy.load()

    for garisX in range(imageinput.width):
        for garisY in range(imageinput.height):
            nilaiR = imageinput.getpixel((garisX, garisY))[0]
            nilaiG = imageinput.getpixel((garisX, garisY))[1]
            nilaiB = imageinput.getpixel((garisX, garisY))[2]
            warna.append([garisX, garisY, nilaiR, nilaiG, nilaiB])
    for data in warna:
        x, y, r, g, b = data
        warnafoto[x, y] = (r, g, b)

    copygambar["image"] = ImageTk.PhotoImage(imgcopy)
    labelcopy = Label(root, image=copygambar["image"])
    labelcopy.grid(row=1, column=2)


def convertimage():
    global imgconvert
    global warna
    convert = []
    option = isi.get()

    if imgconvert is None:
        imgconvert = Image.new("RGB", ukurangambar)

    convert = imgconvert.load()

    for data in warna:
        x, y, r, g, b = data
        if option == 1:
            convert[x, y] = (r, 0, 0)
        elif option == 2:
            convert[x, y] = (0, g, 0)
        elif option == 3:
            convert[x, y] = (0, 0, b)
        elif option == 4:
            convert[x, y] = (0, g, b)
        elif option == 5:
            convert[x, y] = (r, 0, b)
        elif option == 6:
            convert[x, y] = (r, g, 0)

    converting["image"] = ImageTk.PhotoImage(imgconvert)
    labelconvert = Label(root, image=converting["image"])
    labelconvert.grid(row=1, column=3)


def saveimage():
    global imgconvert
    if imgconvert:
        save_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
        if save_file:
            imgconvert.save(save_file)
    else:
        messagebox.showerror("Error", "Tidak ada gambar yang diubah untuk disimpan.")


label1 = Label(root, text="Gambar Asli")
label1.grid(row=0, column=1)
label2 = Label(root, text="Hasil Copy")
label2.grid(row=0, column=2)
label3 = Label(root, text="Hasil Perubahan Warna")
label3.grid(row=0, column=3)

tombolInputGambar = Button(root, text="Buka File", command=openimage)
tombolCopyGambar = Button(root, text="Copy", command=copyimage)
tombolResetGambar = Button(root, text="Reset", command=box)
tombolSimpan = Button(root, text="Simpan Gambar", command=saveimage)

informasi_label = Label(root, text="", justify="left")
informasi_label.grid(row=2, column=1, columnspan=3)

tombolInputGambar.grid(row=3, column=1, sticky=EW)
tombolCopyGambar.grid(row=3, column=2, sticky=EW)
tombolResetGambar.grid(row=3, column=3, sticky=EW)
tombolSimpan.grid(row=4, column=1, columnspan=3, sticky=EW)  # Menggunakan columnspan untuk menggabungkan kolom

isi = IntVar()

CentangRed = ttk.Radiobutton(root, text="Red", variable=isi, value=1, command=convertimage)
CentangGreen = ttk.Radiobutton(root, text="Green", variable=isi, value=2, command=convertimage)
CentangBlue = ttk.Radiobutton(root, text="Blue", variable=isi, value=3, command=convertimage)
CentangCyan = ttk.Radiobutton(root, text="Cyan", variable=isi, value=4, command=convertimage)
CentangMagenta = ttk.Radiobutton(root, text="Magenta", variable=isi, value=5, command=convertimage)
CentangYellow = ttk.Radiobutton(root, text="Yellow", variable=isi, value=6, command=convertimage)

CentangRed.grid(row=4, column=4, sticky=EW)  # Mengganti baris ke 4
CentangGreen.grid(row=5, column=4, sticky=EW)  # Mengganti baris ke 5
CentangBlue.grid(row=6, column=4, sticky=EW)  # Mengganti baris ke 6
CentangCyan.grid(row=4, column=5, sticky=EW)  # Mengganti baris ke 4
CentangMagenta.grid(row=5, column=5, sticky=EW)  # Mengganti baris ke 5
CentangYellow.grid(row=6, column=5, sticky=EW)  # Mengganti baris ke 6

root.mainloop()
