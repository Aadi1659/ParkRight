import csv
import cv2
import os

#counter
i = 0
# Path to the directory containing your CSV files and images
input_directory = 'wrong'
output_directory = 'wrong_parking'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# List of image files in the input directory
image_files = [f for f in os.listdir(input_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
for image_file in image_files:
    image_path = os.path.join(input_directory, image_file)
    csv_file = 'camera.csv' 
    # print(image_path, csv_file)
    with open(csv_file, 'r') as csvfile:
        # print(csvfile)
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row if there is one
        img = cv2.imread(image_path)
        
        for row in csvreader:
            x = int(row[1])
            y = int(row[2])
            w = int(row[3])
            h = int(row[4])
            # Crop the image
            cropped_img = img[y:y+h, x:x+w]
            
            # Save the cropped image with a unique name
            output_filename = f'{i+1}.jpg'
            i = i + 1
            output_path = os.path.join(output_directory, output_filename)
            cv2.imwrite(output_path, cropped_img)
