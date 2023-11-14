# ParkRight
ParkRight is a software which accurately classifies the wrongly parked and correctly parked cars and also empty parked spaces.

# Overview
This project was built using Tensorflow using transfer learning. The main model used was EfficientNetB0 and was trained on approximately 19,000 images with around 6,500 images each of correct parking, wrong parking and empty parking.

# The Project in Action
Here is the video in which the project is being demonstrated: <br>
<video src="https://github.com/Aadi1659/ParkRight/assets/90966493/89b750a7-0946-4872-86ee-6c193f6214aa"/>

# Model
Firstly, download the model from here:
https://drive.google.com/drive/folders/14BdIEtjSl_r6Yia1Q5K5loProtbGSQfN?usp=sharing

# Dataset
The dataset was not available anywhere in the internet. So, I decided to make my own dataset. I used Blender3D to make a 3D model of the parking lot and got a free low poly model of a car. By using my Blender skills, I created 10 images each of correct, wrong and empty parking. 
The required Blender File has been uploaded.
For reference, here is the video: <br>
<video src="https://github.com/Aadi1659/ParkRight/assets/90966493/cb262af7-7a19-4089-b3c8-206e017fc441"/>
<br>
To Download the Dataset, use this link:

# How to run
Install these libraries: open-cv, tensorflow, numpy, streamlit, csv and PIL installed.
<br>
Make sure you do not get errors for any of these lines
```
import cv2
import tensorflow as tf
import numpy as np
import streamlit as st
import csv
from PIL import Image
```
After installing all the dependencies, run <br> 
```
streamlit run app.py
```
You should be able to run the software without any difficulties.
