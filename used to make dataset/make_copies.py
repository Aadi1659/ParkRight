from PIL import Image

# Load the original image
original_image = Image.open('correct/1.png')  # Replace 'your_image.jpg' with your image file

# Number of copies you want to make
num_copies = 100

# Specify a folder to save the copies
output_folder = 'correct/'

# Create the output folder if it doesn't exist
import os
os.makedirs(output_folder, exist_ok=True)

# Make 100 copies of the image
for i in range(num_copies):
    rgb_image = original_image.convert('RGB')
    # Save each copy with a unique filename
    copy_filename = f'{i + 1}.jpg'
    rgb_image.save(copy_filename)

print(f'{num_copies} copies of the image have been created in the "{output_folder}" folder.')
