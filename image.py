import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv,find_dotenv
from PIL import Image
load_dotenv()
genai.configure(api_key="AIzaSyBZUa2gpJGrSbOBzG23dE8LNhPmY4lgdrg") # Do not use this API key


def get_gemini_response(input,image):
    model=genai.GenerativeModel('gemini-2.0-flash')
    response=model.generate_content([input,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="Image Caption Generator App")

st.header("Image Caption Generator App")
#input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","gif"])
image=" "   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", width=300)


submit=st.button("Tell me the Caption")

input_prompt="""
You are an expert in Caption Generation where you need to see the image
               and generate caption as in below format

               Image Format - jpg,jpeg,png,gif
           
            Generated Caption examples

               This image is of a Father carrying his son on his shoulders
               A man drinking water on the streets
               A woman riding a scooter
               
              

"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)


    


