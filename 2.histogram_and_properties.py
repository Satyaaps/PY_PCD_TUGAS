# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya (2205551040)
# 2. Ni Komang Gita Sri Adnyani (2205551010)
# 3. I Putu Nanda Febian Danan Jaya (2205551093)

# *************************************************************************************


from PIL import Image
from PIL.ExifTags import TAGS
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# path to the image or video
imagename = "foto3.jpg"

# read the image data using PIL
image = Image.open(imagename)   

# extract other basic metadata
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

# extract EXIF data
exifdata = image.getexif()

# Create a subplot with two rows and one column
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Display the image in the first subplot
ax1.imshow(image)
ax1.axis('off')  # Turn off axis labels and ticks for the image

# Prepare the text to display in the second subplot
info_text = "\n".join([f"{label}: {value}" for label, value in info_dict.items()])
exif_text = "\n".join([f"{TAGS.get(tag_id, tag_id)}: {exifdata.get(tag_id)}" for tag_id in exifdata])

# Display the text in the second subplot
info_and_exif_text = f"\n\n\nImage Information:\n{info_text}\n\nEXIF Data:\n{exif_text}"
ax2.text(0.05, 0.05, info_and_exif_text, transform=ax2.transAxes,
         fontsize=10, verticalalignment='top')

# Create the histogram in the second subplot
img = cv.imread(imagename)
b, g, r = cv.split(img)
ax2.hist(b.ravel(), 256, [0, 256], color='blue', alpha=0.5, label='Blue Channel')
ax2.hist(g.ravel(), 256, [0, 256], color='green', alpha=0.5, label='Green Channel')
ax2.hist(r.ravel(), 256, [0, 256], color='red', alpha=0.5, label='Red Channel')

# Set labels and legend for the histogram
ax2.set_xlabel('Pixel Value')
ax2.set_ylabel('Frequency')
ax2.legend(loc='upper right')

# Display the histogram and text
plt.tight_layout()
plt.show()