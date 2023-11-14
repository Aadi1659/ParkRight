from PIL import Image, ImageEnhance, ImageFilter
import os

# Specify the folder where your original images are
input_folder = "wrong_parking"

# Specify the folder where you want to save the augmented images
output_folder = "wrong_parking"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List of data augmentation operations you want to apply
# You can customize this list to include the augmentations you want
augmentations = [
    lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),      # Flip the image horizontally
    lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),      # Flip the image vertically
    lambda img: img.rotate(90),                            # Rotate the image by 90 degrees
    lambda img: img.rotate(180),                           # Rotate the image by 180 degrees
    lambda img: img.rotate(270),                           # Rotate the image by 270 degrees
    lambda img: ImageEnhance.Color(img).enhance(0.5),      # Adjust color balance
    lambda img: ImageEnhance.Brightness(img).enhance(1.5), # Adjust brightness
    lambda img: ImageEnhance.Contrast(img).enhance(1.5),   # Adjust contrast
    lambda img: ImageEnhance.Sharpness(img).enhance(2.0),  # Sharpen the image
]

# Function to apply augmentations to an image
def apply_augmentations(image, output_folder, file_number):
    for i, augmentation in enumerate(augmentations):
        augmented_image = augmentation(image.copy())
        output_filename = f"{file_number + i}.jpg"
        output_path = os.path.join(output_folder, output_filename)
        augmented_image.save(output_path)

# Get the starting file number
start_file_number = 141

# Iterate through the original images and apply augmentations
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".png", ".jpeg")):
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        
        # Apply augmentations and save copies
        for i in range(5):  # Create 5 augmented copies for each image
            apply_augmentations(image, output_folder, start_file_number)
            start_file_number += len(augmentations)

print("Data augmentation complete.")
