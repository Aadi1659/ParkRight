import cv2
import tensorflow as tf
import numpy as np
import streamlit as st
import os
import random
import glob
import csv
from PIL import Image
import tensorflow_hub as hub

model = tf.keras.models.load_model('/content/resent.h5',custom_objects={'KerasLayer':hub.KerasLayer})

img_size = (140, 140)

def prepare(img):
    rescale = tf.keras.layers.experimental.preprocessing.Rescaling(scale=1./255, input_shape=(140,140, 3))
    img = rescale(img)
    return img

def display_image(image):
    image = np.array(image)
    st.image(image, caption='Uploaded Image', use_column_width=True)   

def predict(img):
    
    #read the image
    # st.text(img)
    image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    # st.text(img)
    # image = cv2.imread(img)
    csv_path = '/content/drive/MyDrive/ParkRight-master/camera.csv'

    with open(csv_path, newline='') as f:
        boxes = list(csv.reader(f))
    
    #crop images
    image_input = np.zeros(shape=(len(boxes[1:]), img_size[0], img_size[1], 3))
    for i, one_box in enumerate(boxes[1:]):
        one_box_x = int(int(one_box[1]))
        one_box_y = int(int(one_box[2]))
        one_box_w = int(int(one_box[3]))
        one_box_h = int(int(one_box[4]))
        img_resized = cv2.resize(image[one_box_y:one_box_y+one_box_h, one_box_x:one_box_x+one_box_w], img_size,
                                interpolation=cv2.INTER_CUBIC)
        image_input[i] = (prepare(np.expand_dims(img_resized, axis=0)))

    #predict
    #predict the labels
    output = model.predict(image_input)

    #get the label
    label = np.argmax(output, axis=1)

    # Initialize lists to store IDs
    correct_parking_ids = []
    empty_parking_ids = []
    wrong_parking_ids = []

    colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255)]  # Green, Blue, Red

    for i, one_box in enumerate(boxes[1:]):
        one_box_x = int(int(one_box[1]))
        one_box_y = int(int(one_box[2]))
        one_box_w = int(int(one_box[3]))
        one_box_h = int(int(one_box[4]))

        color = colors[label[i]]

        image = cv2.rectangle(image, (one_box_x, one_box_y), (one_box_x + one_box_w, one_box_y + one_box_h),
                        color, 4)
        cv2.putText(image, ('ID:' + str(one_box[0])), (one_box_x, one_box_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color, 2)
        # Append the ID to the appropriate list
        if label[i] == 0:
            correct_parking_ids.append(one_box[0])
        elif label[i] == 1:
            empty_parking_ids.append(one_box[0])
        else:
            wrong_parking_ids.append(one_box[0])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image, caption='Predicted Image', use_column_width=True)
    st.text(f"Number of correct parking: {len(correct_parking_ids)}, IDs: {correct_parking_ids}")
    st.text(f"Number of empty parking: {len(empty_parking_ids)}, IDs: {empty_parking_ids}")
    st.text(f"Number of wrong parking: {len(wrong_parking_ids)}, IDs: {wrong_parking_ids}")
        
def main():
    st.title("ParkRight - Always find a parking spot")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        display_image(image)
        prediction_button = st.button("Analyze")
        if prediction_button:
            predict(img=image)

if __name__ == "__main__":
    main()


