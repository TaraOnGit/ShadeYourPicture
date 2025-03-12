import PIL.Image
import streamlit as st
#import pickle
import cv2
from PIL import Image
import numpy as np

st.title('Picture Shades')

#with open('model.pkl','rb') as f:
 #   model = pickle.load(f)

img = st.file_uploader('Your',type=['png','jpg'])

if(st.button('Show Shades')):

    st.image(img)

    pil_img = PIL.Image.open(img)
    img_arr = np.array(pil_img)
    bw_img = cv2.cvtColor(img_arr,cv2.COLOR_BGR2GRAY)
    st.image(bw_img)
    rgb_img = cv2.cvtColor(img_arr,cv2.COLOR_BGR2RGB)
    st.image(rgb_img)
    st.image(cv2.cvtColor(img_arr,cv2.COLOR_BGR2HSV))




