import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('Model2.h5')
  return model
model=load_model()
st.write("""
# Weather Classfication Group 2 (ADSUARA, CAPALUNGAN)"""
)
file=st.file_uploader("Upload or Select a Sky Picture: Choose any picture of the sky from your device gallery",type=["jpg"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(150,150)
    image=ImageOps.fit(image_data,size,Image.Resampling.LANCZOS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file (JPG)")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names = ["Cloudy", "Rain", "Shine", "Sunrise"]
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)
