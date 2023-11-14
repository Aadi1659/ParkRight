import cv2
import pandas as pd

# Load the CSV file containing coordinates
df = pd.read_csv('camera.csv')

# Load the image
image = cv2.imread('correct_parking.png')  # Replace 'your_image.jpg' with your image file

# Iterate over each row in the CSV file
for index, row in df.iterrows():
    x, y, w, h = row['X'], row['Y'], row['W'], row['H']

    # Draw a rectangle around the object
    color = (0, 255, 0)  # Green color in BGR
    thickness = 2
    image = cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)

# Display the image with the boxes
cv2.imshow('Image with Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
       
            