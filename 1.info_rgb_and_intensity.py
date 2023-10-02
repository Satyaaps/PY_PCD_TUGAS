# ANGGOTA KELOMPOK : 
# 1. I Gede Satya Ariya Putra Sangjaya (2205551040)
# 2. Ni Komang Gita Sri Adnyani (2205551010)
# 3. I Putu Nanda Febian Danan Jaya (2205551093)

# *************************************************************************************


import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_image(image_path, output_file):
    try:
        # Load an image
        image = cv2.imread(image_path)

        if image is None:
            raise FileNotFoundError(f"File '{image_path}' not found.")

        # Get the dimensions of the image
        height, width, _ = image.shape

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Calculate histogram
        hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

        # Open the output file for writing
        with open(output_file, 'w') as file:
            # Output RGB values and coordinates of each pixel
            for y in range(height):
                for x in range(width):
                    intensity = gray_image[y, x]
                    b, g, r = image[y, x]  # Get Blue, Green, and Red values of the pixel
                    file.write(f"({x},{y}) => RGB Value: ({r},{g},{b}), Color Intensity: {intensity}\n")

        # Display the histogram
        plt.figure(figsize=(8, 6))
        plt.title('Grayscale Image Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.plot(hist)
        plt.xlim([0, 256])
        plt.grid(True)
        plt.show()

        # Display the original image
        cv2.imshow('Original Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print(f"Output saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    image_path = 'nanda.jpg'  # Change to your image path
    output_file = 'Image_Info.txt'  # Output file name
    process_image(image_path, output_file)

